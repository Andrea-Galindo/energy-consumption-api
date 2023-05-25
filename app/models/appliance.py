from app import db
from flask import abort, make_response, jsonify

class Appliance(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    power_consumption_watts = db.Column(db.Integer)

    @classmethod
    def from_dict(cls, data_dict):
        return cls(name=data_dict["name"], power_consumption_watts=data_dict["power_consumption_watts"])

    def to_dict(self):
        appliance_dict = {
            "id": self.id,
            "name": self.name,
            "power_consumption_watts": self.power_consumption_watts,
        }

        return appliance_dict

    def update(self, req_body):
        try:
            self.name = req_body["name"]
            self.power_consumption_watts = req_body["power_consumption_watts"]
        except KeyError:
            abort(make_response(jsonify(dict(details="Invalid data")), 400))
            