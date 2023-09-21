from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/application_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app) 


class Role_Listing(db.Model):
    __tablename__ = 'application'
    application_id = db.Column(db.Integer, primary_key= True)
    staff_id = db.Column(db.Integer, nullable=False)
    listing_id = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False)

    def __init__(self, application_id, staff_id, listing_id, status):
        self.application_id = application_id
        self.staff_id = staff_id
        self.listing_id = listing_id
        self.status = status

    def json(self):
        return {"ApplicationID": self.application_id,
                "StaffID": self.staff_id,
                "ListingID": self.listing_id,
                "Status": self.status
                }

# Retrieves every application in the database
@app.route("/application")
def get_all_application():
    applicationlist = Role_Listing.query.all()
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

# Retrieves a application based on application_id
@app.route("/application/<int:application_id>")
def find_by_application_id(application_id):
    application = Role_Listing.query.filter_by(application_id=application_id).first()
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

# Retrieves a application based on staff_id
@app.route("/application/staff/<int:staff_id>")
def find_by_staff_id(staff_id):
    application = Role_Listing.query.filter_by(staff_id=staff_id).first()
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

# Retrieves a application based on listing_id
@app.route("/application/listing/<int:listing_id>")
def find_by_listing_id(listing_id):
    application = Role_Listing.query.filter_by(listing_id=listing_id).first()
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


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5004,debug=True)