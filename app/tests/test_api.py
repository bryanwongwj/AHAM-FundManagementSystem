import json

def test_list(client):
    # Get list of funds and check response
    response = client.get("/fund/")
    assert response.status_code == 200
    assert response.json == [
        {
            "id": 1,
            "name": "TestFund1"
        },
        {
            "id": 2,
            "name": "AHAM Enhanced Deposit Fund"
        },
        {
            "id": 3,
            "name": "AHAM Select Bond Fund"
        }
    ]

def test_get_by_id(client):
    # Get fund by ID and check response
    response = client.get("/fund/3")
    assert response.status_code == 200
    assert response.json == {
        "dscp": "To provide investors with a steady income stream over the medium to long-term period through investments primarily in bonds and other fixed income securities.",
        "dt_create": "2024-11-09 13:59:34",
        "fund_manager_name": "estherteo",
        "id": 3,
        "name": "AHAM Select Bond Fund",
        "nav": 0.5808,
        "performance": 254.612278
    }
    
def test_get_by_invalid_id(client):
    # Get fund by invalid ID and check response
    response = client.get("/fund/99999")
    assert response.status_code == 404
    assert response.json["message"] == "Fund not found."
    
def test_create_update_delete(client):
    # Create new fund
    response = client.post("/fund/", json={
        "name": "AHAM Enhanced Deposit Fund",
        "performance": 183.644138,
        "fund_manager_name": "johndoe",
        "dscp": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "nav": 1.2253
    })
    assert response.status_code == 201
    
    res_dict = response.json
    new_id = res_dict.get("id")
    
    # Check if id and dt_create is not empty
    assert new_id is not None
    assert res_dict.get("dt_create") is not None
    
    # Remove id and dt_create to check remaining fields
    res_dict.pop("id")
    res_dict.pop("dt_create")
    assert res_dict == {
        "name": "AHAM Enhanced Deposit Fund",
        "performance": 183.644138,
        "fund_manager_name": "johndoe",
        "dscp": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "nav": 1.2253
    }
    
    # Update performance of created fund
    response = client.put("/fund/" + str(new_id), json={
        "performance": 235.493029
    })
    assert response.status_code == 200
    
    # Check if id and dt_create is not empty
    res_dict = response.json
    new_id = res_dict.get("id")
    assert new_id is not None
    assert res_dict.get("dt_create") is not None
    
    # Remove id and dt_create to check remaining fields
    res_dict.pop("id")
    res_dict.pop("dt_create")
    assert res_dict == {
        "name": "AHAM Enhanced Deposit Fund",
        "performance": 235.493029,
        "fund_manager_name": "johndoe",
        "dscp": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "nav": 1.2253
    }
    
    # Delete created fund
    response = client.delete("/fund/" + str(new_id))
    assert response.status_code == 204
    
def test_create_without_required(client):
    # Create new fund without required fields and check response
    response = client.post("/fund/", json={
        "dscp": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    })
    assert response.status_code == 422
    assert response.json["errors"]["json"] == {
        "fund_manager_name": [
            "Missing data for required field."
        ],
        "name": [
            "Missing data for required field."
        ],
        "nav": [
            "Missing data for required field."
        ],
        "performance": [
            "Missing data for required field."
        ]
    }
    
def test_create_max_length(client):
    # Create new fund with string fields exceeding maximum length
    response = client.post("/fund/", json={
        "name": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nisi sem, dictum id sem eget, bibendum condimentum odio",
        "performance": 183.644138,
        "fund_manager_name": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nisi sem, dictum id sem eget, bibendum condimentum odio",
        "dscp": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nisi sem, dictum id sem eget, bibendum condimentum odio. Duis ac enim ac massa tincidunt sodales ac eu urna. Donec a odio volutpat, ultrices elit ut, sodales massa.",
        "nav": 1.2253
    })
    assert response.status_code == 422
    assert response.json["errors"]["json"] == {
        "dscp": [
            "Longer than maximum length 200."
        ],
        "fund_manager_name": [
            "Longer than maximum length 50."
        ],
        "name": [
            "Longer than maximum length 50."
        ]
    }
    
def test_create_invalid_values(client):
    # Create new fund using invalid values
    response = client.post("/fund/", json={
        "name": 183.644138,
        "performance": "AHAM Enhanced Deposit Fund",
        "fund_manager_name": 1.2253,
        "dscp": 183.644138,
        "nav": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    })
    assert response.status_code == 422
    assert response.json["errors"]["json"] == {
        "dscp": [
            "Not a valid string."
        ],
        "fund_manager_name": [
            "Not a valid string."
        ],
        "name": [
            "Not a valid string."
        ],
        "nav": [
            "Not a valid number."
        ],
        "performance": [
            "Not a valid number."
        ]
    }
    
def test_update_invalid_id(client):
    # Update fund by invalid id
    response = client.put("/fund/99999", json={
        "performance": 235.493029
    })
    assert response.status_code == 404
    assert response.json["message"] == "Fund not found."
    
def test_update_without_required(client):
    # Update existing fund without required fields and check response
    response = client.put("/fund/2", json={})
    assert response.status_code == 422
    assert response.json["errors"]["json"] == {
        "performance": [
            "Missing data for required field."
        ]
    }
    
def test_update_invalid_values(client):
    # Update existing fund using invalid values
    response = client.put("/fund/2", json={
        "performance": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
    })
    assert response.status_code == 422
    assert response.json["errors"]["json"] == {
        "performance": [
            "Not a valid number."
        ]
    }
    
def test_delete_invalid_id(client):
    # Delete fund by invalid id
    response = client.delete("/fund/99999")
    assert response.status_code == 404
    assert response.json["message"] == "Fund not found."
            