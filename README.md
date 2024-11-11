# AHAM Fund Management System

RESTful API for a fund management company.

## API documentation
### Fund API

<details>
 <summary><code>GET</code> <code><b>/fund/</b></code> <code>(List all funds)</code></summary>

#### Responses
##### `200` OK
> ```
> [
>   {
>     "id": 1,
>     "name": "AHAM Enhanced Deposit Fund"
>   }
> ]
> ```
##### `500` Internal Server Error
> ```
> {
>   "code": 500,
>   "message": "Internal server error.",
>   "status": "Internal Server Error"
> }
> ```
#### Example cURL
> ```javascript
>curl -X 'GET' \
>    'http://127.0.0.1:5000/fund/' \
>    -H 'accept: application/json'
> ```

</details>

<details>
 <summary><code>POST</code> <code><b>/fund/</b></code> <code>(Create a new fund)</code></summary>

#### Request
##### Header
> | name            |  value            |
> |-----------------|-------------------|
> | accept          |  application/json |
> | Content-Type    |  application/json |

##### Body
> ```
> {
>   "name": "AHAM Enhanced Deposit Fund",
>   "performance": 183.644138,
>   "fund_manager_name": "johndoe",
>   "dscp": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
>   "nav": 1.2253
> }
> ```
#### Responses
##### `200` OK
> ```
> [
>   {
>     "id": 1,
>     "name": "AHAM Enhanced Deposit Fund"
>   }
> ]
> ```
##### `422` Unprocessable Entity
> ```
> {
>   "code": 422,
>   "errors": {
>     "json": {
>       "name": [
>         "Not a valid string."
>       ]
>     }
>   },
>   "status": "Unprocessable Entity"
> }
> ```
##### `500` Internal Server Error
> ```
> {
>   "code": 500,
>   "message": "Internal server error.",
>   "status": "Internal Server Error"
> }
> ```
#### Example cURL
> ```javascript
>curl -X 'POST' \
>    'http://127.0.0.1:5000/fund/' \
>    -H 'accept: application/json' \
>    -H 'Content-Type: application/json' \
>    -d '{
>    "name": "AHAM Enhanced Deposit Fund",
>    "performance": 183.644138,
>    "fund_manager_name": "johndoe",
>    "dscp": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
>    "nav": 1.2253
>}'
> ```

</details>

<details>
 <summary><code>GET</code> <code><b>/fund/{fund_id}</b></code> <code>(Get fund by ID)</code></summary>

#### Parameters
> | name              |  type     | data type      | description                         |
> |-------------------|-----------|----------------|-------------------------------------|
> | `fund_id`         |  required | string         | Fund ID                             |

#### Responses
##### `200` OK
> ```
> {
>   "id": 1,
>   "name": "AHAM Enhanced Deposit Fund",
>   "performance": 183.644138,
>   "fund_manager_name": "johndoe",
>   "dscp": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
>   "dt_create": "2024-11-09 08:57:31",
>   "nav": 1.2253
> }
> ```
##### `500` Internal Server Error
> ```
> {
>   "code": 500,
>   "message": "Internal server error.",
>   "status": "Internal Server Error"
> }
> ```
#### Example cURL
> ```javascript
>curl -X 'GET' \
>    'http://127.0.0.1:5000/fund/1' \
>    -H 'accept: application/json'
> ```

</details>

<details>
 <summary><code>PUT</code> <code><b>/fund/{fund_id}</b></code> <code>(Update performance of existing fund by ID)</code></summary>

#### Parameters
> | name              |  type     | data type      | description                         |
> |-------------------|-----------|----------------|-------------------------------------|
> | `fund_id`         |  required | string         | Fund ID                             |

#### Request
##### Header
> | name            |  value            |
> |-----------------|-------------------|
> | accept          |  application/json |
> | Content-Type    |  application/json |

##### Body
> ```
> {
>   "performance": 183.644138
> }
> ```
#### Responses
##### `200` OK
> ```
> {
>   "id": 1,
>   "name": "AHAM Enhanced Deposit Fund",
>   "performance": 183.644138,
>   "fund_manager_name": "johndoe",
>   "dscp": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
>   "dt_create": "2024-11-09 08:57:31",
>   "nav": 1.2253
> }
> ```
##### `422` Unprocessable Entity
> ```
> {
>   "code": 422,
>   "errors": {
>     "json": {
>       "performance": [
>         "Not a valid number."
>       ]
>     }
>   },
>   "status": "Unprocessable Entity"
> }
> ```
##### `500` Internal Server Error
> ```
> {
>   "code": 500,
>   "message": "Internal server error.",
>   "status": "Internal Server Error"
> }
> ```
#### Example cURL
> ```javascript
>curl -X 'PUT' \
>    'http://127.0.0.1:5000/fund/1' \
>    -H 'accept: application/json' \
>    -H 'Content-Type: application/json' \
>    -d '{
>    "performance": 183.644138
>}'
> ```
</details>

<details>
 <summary><code>DELETE</code> <code><b>/fund/{fund_id}</b></code> <code>(Delete fund by ID)</code></summary>

#### Parameters
> | name              |  type     | data type      | description                         |
> |-------------------|-----------|----------------|-------------------------------------|
> | `fund_id`         |  required | string         | Fund ID                             |

#### Responses
##### `204` No Content
##### `500` Internal Server Error
> ```
> {
>   "code": 500,
>   "message": "Internal server error.",
>   "status": "Internal Server Error"
> }
> ```
#### Example cURL
> ```javascript
>curl -X 'DELETE' \
>    'http://127.0.0.1:5000/fund/1' \
>    -H 'accept: application/json'
> ```

</details>

## Database documentation (PostgreSQL)

### Table schema
#### fund_managers
| Column Name        |  Data Type       |  Type             | Description                         |
|--------------------|------------------|-------------------|-------------------------------------|
| id                 |  int             | Primary Key       | Fund Manager ID                     |
| name               |  string          | Unique Key        | Fund Manager name                   |

#### funds
| Column Name        |  Data Type                       |  Type                             | Description                         |
|--------------------|----------------------------------|-----------------------------------|-------------------------------------|
| id                 |  int                             | Primary Key                       | Fund ID                             |
| name               |  string                          |                                   | Fund name                           |
| fund_manager_id    |  int                             | Foreign Key (fund_managers.id)    | Fund Manager ID                     |
| dscp               |  string                          |                                   | Fund description                    |
| nav                |  double precision                |                                   | Fund NAV                            |
| dt_create          |  timestamp without time zone     |                                   | Fund date of creation               |
| performance        |  double precision                |                                   | Fund performance                    |


## Deploy using Docker Compose (Linux)

1. Install the required dependencies
    * Docker
2. Clone the repository
3. Add `psycopg2-binary` in `requirements.txt` for PostgreSQL support
4. Modify `docker-compose.yml` if necessary
5. Start the server and PostgreSQL database using Docker Compose
    * The `--build` option is necessary when starting the server for the first time
```
docker-compose up --build
```

## Local development (Windows)

1. Install the required dependencies
    * Python 3.8+
    * pip
2. Clone the repository
3. Create a python virtual environment
```
pip install virtualenv
python -m venv .venv
```
4. Install the python dependencies required for this project
```
pip install --no-cache-dir -r requirements.txt
```
5. Start the development server
```
python run.py
```
6. The server should now be runinng on http://127.0.0.1:5000
    * If FLASK_ENV is set to `development`, Swagger UI is avaliable on http://127.0.0.1:5000/docs
    * The respective SQLite databases located in the `instance` folder will be used when FLASK_ENV is set to `development` and `testing`
7. Tests can be executed using the following command
```
pytest
```