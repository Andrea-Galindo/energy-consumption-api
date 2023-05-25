from app import db
from app.models.appliance import Appliance
from flask import Blueprint, jsonify, make_response, request, abort
from app.routes.routes_helper import validate_model, validate_input_data, error_message

appliances_bp = Blueprint("appliances_bp", __name__, url_prefix="/appliances")