from app import db
from flask import abort, make_response, jsonify

class Appliance(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    power_consumption_watts = db.Column(db.Integer)