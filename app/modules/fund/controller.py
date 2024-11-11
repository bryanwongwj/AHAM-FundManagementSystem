from app.db.db import *

class FundController:
    def get_list(self):
        return [
            db_fund.to_dict() for db_fund in db.session.query(Fund).order_by(Fund.id)
        ]
        
    def get_by_id(self, id):
        db_fund = db.session.query(Fund).filter(Fund.id == id).first()
        
        if db_fund is None:
            raise ValueError("Fund not found.")
        
        return db_fund.to_dict()
    
    def create(self, fund):
        fund_manager_name = fund["fund_manager_name"]
        db_fund_manager = db.session.query(FundManager).filter(FundManager.name == fund_manager_name).first()
        
        # create new fund manager if fund manager name does not exist
        if db_fund_manager is None:
            db_fund_manager = FundManager(name=fund_manager_name)
            db.session.add(db_fund_manager)
            db.session.commit()
            
        db_fund: Fund = Fund(**{k: fund[k] for k in fund if k not in {"fund_manager_name"}})
        db_fund.fund_manager_id = db_fund_manager.id
        db.session.add(db_fund)
        db.session.commit()
        
        return db_fund.to_dict()
    
    def update_performance(self, id, update_data):
        db_fund = db.session.query(Fund).filter(Fund.id == id).first()
        
        if db_fund is None:
            raise ValueError("Fund not found.")
        
        db_fund.performance = update_data["performance"]
        db.session.commit()
        
        return db_fund.to_dict()
    
    def delete(self, id):
        db_fund = db.session.query(Fund).filter(Fund.id == id).first()
        
        if db_fund is None:
            raise ValueError("Fund not found.")
        
        db.session.delete(db_fund)
        db.session.commit()
