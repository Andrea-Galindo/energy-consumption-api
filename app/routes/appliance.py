from app import db
from app.models.appliance import Appliance
from flask import Blueprint, jsonify, make_response, request, abort
from app.routes.routes_helper import validate_model, validate_input_data, error_message

appliances_bp = Blueprint("appliances_bp", __name__, url_prefix="/appliances")

# read one appliance (GET)
@appliances_bp.route("/<id>", methods=["GET"])
def read_one_appliance(id):
    appliance = validate_model(Appliance, id)

    return jsonify({"appliance": appliance.to_dict()}), 200

# read all appliances (GET)
@appliances_bp.route("", methods=["GET"])
def read_all_appliances():
     # if in url we add a query param -> /appliances?name=stove
    sort_asc_query = request.args.get("sort")

    if sort_asc_query == "asc": 
        appliances = Appliance.query.order_by(Appliance.name)
    elif sort_asc_query == "desc":
        appliances = Appliance.query.order_by(Appliance.name.desc())
    else:
        appliances = Appliance.query.all()

    appliances_response = [appliance.to_dict() for appliance in appliances]

    return jsonify(appliances_response)

# create an appliance (POST)
@appliances_bp.route("", methods=["POST"])
def create_appliance():
    request_body = request.get_json()

    new_appliance = validate_input_data(Appliance, request_body)

    db.session.add(new_appliance)
    db.session.commit()

#     return jsonify({"appliance": new_appliance.to_dict()}), 201

# # replace an appliance (PUT)
# @appliances_bp.route("/<id>", methods=["PUT"])
# def update_appliance(id):
#     appliance = validate_model(Appliance, id)

#     request_body = request.get_json()

#     appliance.update(request_body)

#     db.session.commit()
   
#     response = {"appliance": appliance.to_dict()}
#     return response
    
# # delete a appliance (DELETE)
# @appliances_bp.route("/<id>", methods=["DELETE"])
# def delete_appliance(id):
#     appliance = validate_model(Appliance, id)

#     # saves name before being deleted 
#     name = appliance.name

#     db.session.delete(appliance)
#     db.session.commit()
    
#     return(make_response({"details": f"appliance {id} {name} successfully deleted"}), 200)
