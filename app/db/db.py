from typing import List, Optional
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy as sa
from sqlalchemy.orm import (
    DeclarativeBase,
    relationship,
    Mapped,
    mapped_column
)

from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlite3 import Connection as SQLite3Connection

# Enable foreign key constraint when using SQLite database
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()

class Base(DeclarativeBase):
    pass

db = sa(model_class=Base)

class FundManager(Base):
    __tablename__ = "fund_managers"
    __table_args__ = (
        db.UniqueConstraint("name", name="uk_fund_manager_name"),
    )
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(50))
    funds: Mapped[List["Fund"]] = relationship(
        "Fund", back_populates="fund_manager"
    )
    
class Fund(Base):
    __tablename__ = "funds"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(50))
    fund_manager_id: Mapped[int] = mapped_column(db.ForeignKey("fund_managers.id"), nullable=False, index=True)
    fund_manager: Mapped["FundManager"] = relationship(
        "FundManager", back_populates="funds"
    )
    dscp: Mapped[Optional[str]] = mapped_column(db.String(200))
    nav: Mapped[float]
    dt_create: Mapped[datetime] = mapped_column(db.DateTime, server_default=db.func.now())
    performance: Mapped[float]
    
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "fund_manager_name": self.fund_manager.name,
            "dscp": self.dscp,
            "nav": self.nav,
            "dt_create": self.dt_create,
            "performance": self.performance
        }
    