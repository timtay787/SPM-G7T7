from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_cors import CORS
from datetime import datetime
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/sbrp_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app) 


class Role_Application(db.Model):
    __tablename__ = 'role_application'
    role_app_id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    role_listing_id = db.Column(db.Integer, nullable=False)
    staff_id = db.Column(db.Integer, nullable=False)
    role_app_status = db.Column(db.String(20), nullable=False)
    role_app_ts_create = db.Column(db.DateTime, nullable=False)
    reason_for_application = db.Column(db.String(50000), nullable=False)

    def __init__(self, role_listing_id, staff_id, role_app_status, role_app_ts_create, reason_for_application):
        self.role_listing_id = role_listing_id
        self.staff_id = staff_id
        self.role_app_status = role_app_status
        self.role_app_ts_create = role_app_ts_create
        self.reason_for_application = reason_for_application

    def json(self):
        return {"RoleApplicationID": self.role_app_id,
                "RoleListingID": self.role_listing_id,
                "StaffID": self.staff_id,
                "RoleApplicationStatus": self.role_app_status,
                "RoleApplicationTimestampCreate": self.role_app_ts_create,
                "ReasonForApplication": self.reason_for_application
                }
    
# Creates a new application
# Sample imput:
# {"role_listing_id": 3,
# "staff_id": 4}  
@app.route("/role_application", methods=['POST'])
def create_application():
    data = request.get_json()
    application = Role_Application(data["role_listing_id"], data["staff_id"], "applied", func.now(), data["reason_for_application"])

    # checks if application with same role_listing_id and staff_id exists
    application_check = Role_Application.query.filter_by(role_listing_id=data["role_listing_id"], staff_id=data["staff_id"]).first()
    if application_check:
        return jsonify(
            {
                "code": 400,
                "data": application_check.json(),
                "message": "You have already applied for this role."
            }
        ), 400
    else:
        try:
            db.session.add(application)
            db.session.commit()
        except:
            return jsonify(
                {
                    "code": 500,
                    "data": {
                        "application": application.json()
                    },
                    "message": "An error occurred creating the application."
                }
            ), 500
        return jsonify(
            {
                "code": 201,
                "data": application.json(),
                "message": "Application created successfully."
            }
        ), 201


# Withdraws an application
@app.route("/role_application/withdraw/<int:application_id>", methods=['PUT'])
def withdraw_application(application_id):
    application = Role_Application.query.filter_by(role_app_id=application_id).first()
    if application:
        application.role_app_status = "withdrawn"
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": application.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "application_id": application_id
            },
            "message": "Application not found."
        }
    ), 404

# Retrieves every application in the database
@app.route("/role_application")
def get_all_application():
    applicationlist = Role_Application.query.all()
    if len(applicationlist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "application": [application.json() for application in applicationlist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no applications."
        }
    ), 404

# Retrieves an application based on application_id
@app.route("/role_application/<int:application_id>")
def find_by_application_id(application_id):
    application = Role_Application.query.filter_by(role_app_id=application_id).first()
    if application:
        return jsonify(
            {
                "code": 200,
                "data": application.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Application not found."
        }
    ), 404

# Retrieves every application based on staff_id
@app.route("/role_application/staff/<int:staff_id>")
def find_by_staff_id(staff_id):
    applicationList = Role_Application.query.filter_by(staff_id=staff_id).all()
    if len(applicationList):
        return jsonify(
            {
                "code": 200,
                "data":{
                    "application": [application.json() for application in applicationList]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Application not found."
        }
    ), 404

# Retrieves applications based on listing_id
@app.route("/role_application/listing/<int:listing_id>")
def find_by_listing_id(listing_id):
    application = Role_Application.query.filter_by(role_listing_id=listing_id).all()
    if application:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "application": [application.json() for application in application]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Application not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5004,debug=True)