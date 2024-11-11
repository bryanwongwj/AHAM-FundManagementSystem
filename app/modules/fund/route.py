from flask import Flask
from flask.views import MethodView
import marshmallow as ma
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from .controller import FundController
from .model import *


fund_bp = Blueprint("fund", "fund", url_prefix="/fund", description="Fund API")
fund_controller = FundController()

@fund_bp.route("/")
class Fund(MethodView):
    @fund_bp.response(200, FundSchema(many=True))
    def get(self):
        """List all funds"""
        try:
            fund_list = fund_controller.get_list()
        except SQLAlchemyError:
            abort(500, message="Internal server error.")
        return fund_list

    @fund_bp.arguments(FundDetailSchema)
    @fund_bp.response(201, FundDetailSchema)
    def post(self, new_data):
        """Create a new fund"""
        try:
            fund = fund_controller.create(new_data)
        except SQLAlchemyError:
            abort(500, message="Internal server error.")
        return fund


@fund_bp.route("/<fund_id>")
class FundById(MethodView):
    @fund_bp.response(200, FundDetailSchema)
    def get(self, fund_id):
        """Get fund by ID"""
        try:
            fund = fund_controller.get_by_id(fund_id)
        except ValueError as e:
            abort(404, message=str(e))
        except SQLAlchemyError:
            abort(500, message="Internal server error.")
        return fund

    @fund_bp.arguments(FundUpdateSchema)
    @fund_bp.response(200, FundDetailSchema)
    def put(self, update_data, fund_id):
        """Update performance of existing fund by ID"""
        try:
            fund = fund_controller.update_performance(fund_id, update_data)
        except ValueError as e:
            abort(404, message=str(e))
        except SQLAlchemyError:
            abort(500, message="Internal server error.")
        return fund

    @fund_bp.response(204)
    def delete(self, fund_id):
        """Delete fund by ID"""
        try:
            fund_controller.delete(fund_id)
        except ValueError as e:
            abort(404, message=str(e))
        except SQLAlchemyError:
            abort(500, message="Internal server error.")
      