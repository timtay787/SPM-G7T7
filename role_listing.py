from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/role_listing_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app) 


class Role_Listing(db.Model):
    __tablename__ = 'role_listings'
    Role_Listing_ID = db.Column(db.Integer, primary_key= True)
    Role_ID = db.Column(db.Integer, nullable=False)
    Role_Listing_Desc = db.Column(db.String(50000), nullable=False)
    Role_Listing_Source = db.Column(db.Integer, primary_key= True)
    Role_Listing_Open = db.Column(db.Date, nullable=False)
    Role_Listing_Close = db.Column(db.Date, nullable=False)
    Role_Listing_Creator = db.Column(db.Integer, nullable=False)
    Role_Listing_ts_create = db.Column(db.DateTime, nullable=False)
    Country = db.Column(db.String(50), nullable=False)
    Career_Level = db.Column(db.String(50), nullable=False)
    Role_Listing_Updater = db.Column(db.Integer, nullable=False)
    Role_Listing_ts_update = db.Column(db.DateTime, nullable=False)

    def __init__(self, Role_Listing_ID, Role_ID, Role_Listing_Desc, Role_Listing_Source, Role_Listing_Open, Role_Listing_Close, Role_Listing_Creator, Role_Listing_ts_create, Country, Career_Level, Role_Listing_Updater, Role_Listing_ts_update):
        self.Role_Listing_ID = Role_Listing_ID
        self.Role_ID = Role_ID
        self.Role_Listing_Description = Role_Listing_Desc
        self.Role_Listing_Source = Role_Listing_Source
        self.Role_Listing_Open = Role_Listing_Open
        self.Role_Listing_Close = Role_Listing_Close
        self.Role_Listing_Creator = Role_Listing_Creator
        self.Role_Listing_ts_create = Role_Listing_ts_create
        self.Country = Country
        self.Career_Level = Career_Level
        self.Role_Listing_Updater = Role_Listing_Updater
        self.Role_Listing_ts_update = Role_Listing_ts_update

    def json(self):
        return {"RoleListingID": self.Role_Listing_ID,
                "RoleID": self.Role_ID,
                "RoleListingDescription": self.Role_Listing_Desc,
                "RoleListingSource": self.Role_Listing_Source,
                "RoleListingOpen": self.Role_Listing_Open,
                "RoleListingClose": self.Role_Listing_Close,
                "RoleListingCreator": self.Role_Listing_Creator,
                "RoleListingTimestampCreate": self.Role_Listing_ts_create,
                "Country": self.Country,
                "CareerLevel": self.Career_Level,
                "RoleListingUpdater": self.Role_Listing_Updater,
                "RoleListingTimestampUpdate": self.Role_Listing_ts_update
                }

class Candidates(db.Model):
    __tablename__ = 'candidates'
    Candidate_ID = db.Column(db.Integer, primary_key= True)
    Role_Listing_ID = db.Column(db.Integer, primary_key= True)

    def __init__(self, Candidate_ID, Role_Listing_ID):
        self.Candidate_ID = Candidate_ID
        self.Role_Listing_ID = Role_Listing_ID
    
    def json(self):
        return {"CandidateID": self.Candidate_ID,
                "RoleListingID": self.Role_Listing_ID
                }

# Retrieves every role_listing in the database
@app.route("/role_listing")
def get_all_role_listing():
    role_listinglist = Role_Listing.query.all()
    if len(role_listinglist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "role_listing": [role_listing.json() for role_listing in role_listinglist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no role_listings."
        }
    ), 404


# Retrieves a role_listing based on listing_id
@app.route("/role_listing/<int:listing_id>")
def find_by_listing_id(listing_id):
    role_listing = Role_Listing.query.filter_by(Role_Listing_ID=listing_id).first()
    if role_listing:
        return jsonify(
            {
                "code": 200,
                "data": role_listing.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Role Listing not found."
        }
    ), 404

# Retrieves role listings based on role_id
@app.route("/role_listing/role/<int:role_id>")
def find_by_role_id(role_id):
    role_listing = Role_Listing.query.filter_by(Role_ID=role_id).all()
    if len(role_listing):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "role_listing": [role_listing.json() for role_listing in role_listing]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Role Listing not found."
        }
    ), 404

# Retrieves candidates based on role_listing_id
@app.route("/role_listing/candidates/<int:role_listing_id>")
def find_by_role_listing_id(role_listing_id):
    candidates = Candidates.query.filter_by(Role_Listing_ID=role_listing_id).all()
    if len(candidates):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "candidates": [candidate.json() for candidate in candidates]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Candidates not found."
        }
    ), 404

# Retrieves a specific candidate based on candidate id and role_listing id
@app.route("/role_listing/candidates/<int:role_listing_id>/<int:candidate_id>")
def find_by_candidate_id(candidate_id, role_listing_id):
    candidate = Candidates.query.filter_by(Candidate_ID=candidate_id, Role_Listing_ID=role_listing_id).first()
    if candidate:
        return jsonify(
            {
                "code": 200,
                "data": candidate.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Candidate not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5003,debug=True)