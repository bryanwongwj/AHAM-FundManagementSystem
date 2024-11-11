import pytest
import unittest
import json

from app.db.db import *
from sqlalchemy.exc import IntegrityError, StatementError

def test_fund_insert_update_delete(app):
    with app.app_context():
        # Insert new record in funds table using existing fund manager id
        fund_dict = {
            "name": "AHAM Enhanced Deposit Fund",
            "performance": 183.644138,
            "fund_manager_id": "3",
            "dscp": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "nav": 1.2253
        }
        db_fund: Fund = Fund(**fund_dict)
        db.session.add(db_fund)
        db.session.commit()
        
        inserted_id = db_fund.id
        
        # Check if record is inserted properly
        db_fund_new = db.session.query(Fund).filter(Fund.id == inserted_id).first()
        assert db_fund_new.name == "AHAM Enhanced Deposit Fund"
        assert db_fund_new.performance == 183.644138
        assert db_fund_new.fund_manager_id == 3
        assert db_fund_new.dscp == "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        assert db_fund_new.nav == 1.2253
        
        # Update record
        db_fund_new.performance = 293.392839
        db.session.commit()
        
        # Check if record is updated properly
        db_fund_new = db.session.query(Fund).filter(Fund.id == inserted_id).first()
        assert db_fund_new.name == "AHAM Enhanced Deposit Fund"
        assert db_fund_new.performance == 293.392839
        assert db_fund_new.fund_manager_id == 3
        assert db_fund_new.dscp == "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        assert db_fund_new.nav == 1.2253
        
        # Delete record
        db_fund_new = db.session.query(Fund).filter(Fund.id == inserted_id).first()
        db.session.delete(db_fund_new)
        db.session.commit()
        
        # Check if record is deleted properly
        db_fund_new = db.session.query(Fund).filter(Fund.id == inserted_id).first()
        assert db_fund_new is None
        
@pytest.mark.xfail(raises=IntegrityError)
def test_fund_insert_duplicate_id(app):
    with app.app_context():
        # Insert new record in funds table using an ID that already exists
        fund_dict = {
            "id": 1,
            "name": "AHAM Enhanced Deposit Fund",
            "performance": 183.644138,
            "fund_manager_id": "99999",
            "dscp": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "nav": 1.2253
        }
        db_fund: Fund = Fund(**fund_dict)
        db.session.add(db_fund)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()

@pytest.mark.xfail(raises=IntegrityError)
def test_fund_insert_invalid_fund_manager(app):
    with app.app_context():
        # Insert new record in funds table with invalid fund manager id
        fund_dict = {
            "name": "AHAM Enhanced Deposit Fund",
            "performance": 183.644138,
            "fund_manager_id": "99999",
            "dscp": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            "nav": 1.2253
        }
        db_fund: Fund = Fund(**fund_dict)
        db.session.add(db_fund)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            
@pytest.mark.xfail(raises=IntegrityError)
def test_fund_insert_wihtout_required(app):
    with app.app_context():
        # Insert new record in funds table without required fields
        fund_dict = {
            "dscp": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        }
        db_fund: Fund = Fund(**fund_dict)
        db.session.add(db_fund)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            
@pytest.mark.xfail(raises=StatementError)
def test_fund_insert_invalid_data(app):
    with app.app_context():
        # Insert new record in funds table with invalid data
        fund_dict = {
            "name": 183.644138,
            "performance": "AHAM Enhanced Deposit Fund",
            "fund_manager_id": 2,
            "dscp": 183.644138,
            "nav": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        }
        db_fund: Fund = Fund(**fund_dict)
        db.session.add(db_fund)
        try:
            db.session.commit()
        except StatementError:
            db.session.rollback()
            
def test_fund_manager_insert_delete(app):
    with app.app_context():
        # Insert new record in fund managers table
        fund_manager_dict = {
            "name": "testfundmanager"
        }
        db_fund_manager: FundManager = FundManager(**fund_manager_dict)
        db.session.add(db_fund_manager)
        db.session.commit()
        
        inserted_id = db_fund_manager.id
        
        # Check if record is inserted properly
        db_fund_manager_new = db.session.query(FundManager).filter(FundManager.id == inserted_id).first()
        assert db_fund_manager_new.name == "testfundmanager"
        
        # Delete record
        db_fund_manager_new = db.session.query(FundManager).filter(FundManager.id == inserted_id).first()
        db.session.delete(db_fund_manager_new)
        db.session.commit()
        
        # Check if record is deleted properly
        db_fund_manager_new = db.session.query(FundManager).filter(FundManager.id == inserted_id).first()
        assert db_fund_manager_new is None
            
@pytest.mark.xfail(raises=IntegrityError)
def test_fund_manager_insert_duplicate_id(app):
    with app.app_context():
        # Insert new record in fund managers table using an ID that already exists
        fund_manager_dict = {
            "id": 1,
            "name": "testfundmanager"
        }
        db_fund_manager: Fund = Fund(**fund_manager_dict)
        db.session.add(db_fund_manager)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            
@pytest.mark.xfail(raises=IntegrityError)
def test_fund_manager_insert_duplicate_name(app):
    with app.app_context():
        # Insert new record in fund managers table using a name that already exists
        fund_manager_dict = {
            "name": "bryanwongwj"
        }
        db_fund_manager: Fund = Fund(**fund_manager_dict)
        db.session.add(db_fund_manager)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            
@pytest.mark.xfail(raises=IntegrityError)
def test_fund_manager_delete_child_exists(app):
    with app.app_context():
        # Delete existing record when child record in funds table still exists
        db_fund_manager = db.session.query(FundManager).filter(FundManager.id == 2).first()
        db.session.delete(db_fund_manager)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()