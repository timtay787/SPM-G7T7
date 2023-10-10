from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_cors import CORS
from datetime import datetime

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
    Role_Listing_Source = db.Column(db.Integer, nullable=False)
    Role_Listing_Open = db.Column(db.Date, nullable=False)
    Role_Listing_Close = db.Column(db.Date, nullable=False)
    Role_Listing_Creator = db.Column(db.Integer, nullable=False)
    Role_Listing_ts_create = db.Column(db.DateTime, nullable=False)
    # Country = db.Column(db.String(50), nullable=False)
    # Career_Level = db.Column(db.String(50), nullable=False)
    Role_Listing_Updater = db.Column(db.Integer, nullable=False)
    Role_Listing_ts_update = db.Column(db.DateTime, nullable=False)

    def __init__(self, Role_Listing_ID, Role_ID, Role_Listing_Desc, Role_Listing_Source, Role_Listing_Open, Role_Listing_Close, Role_Listing_Creator, Role_Listing_ts_create, Role_Listing_Updater, Role_Listing_ts_update):
        self.Role_Listing_ID = Role_Listing_ID
        self.Role_ID = Role_ID
        self.Role_Listing_Desc = Role_Listing_Desc
        self.Role_Listing_Source = Role_Listing_Source
        self.Role_Listing_Open = Role_Listing_Open
        self.Role_Listing_Close = Role_Listing_Close
        self.Role_Listing_Creator = Role_Listing_Creator
        self.Role_Listing_ts_create = Role_Listing_ts_create
        # self.Country = Country
        # self.Career_Level = Career_Level
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
                # "Country": self.Country,
                # "CareerLevel": self.Career_Level,
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
    
# Creates a new role_listing
# Sample input:
# {
#     "Role_Listing_ID": 4,
#     "Role_ID": 1,
#     "Role_Listing_Desc": "This is a test role listing.",
#     "Role_Listing_Source": 1,
#     "Role_Listing_Close": "2021-01-01",
#     "Role_Listing_Creator": 2
# }
@app.route("/role_listing", methods=['POST'])
def create_role_listing():
    data = request.get_json()
    current_time = datetime.now()
    current_date = current_time.date()
    
    role_listing = Role_Listing(data["Role_Listing_ID"], data["Role_ID"], data["Role_Listing_Desc"], data["Role_Listing_Source"], current_date, data["Role_Listing_Close"], data["Role_Listing_Creator"], func.now(), 0, '')
    role_listing_check = Role_Listing.query.filter_by(Role_Listing_ID=data["Role_Listing_ID"]).first()
    if role_listing_check:
        return jsonify(
            {
                "code": 400,
                "data": {
                    "role_listing": role_listing.json()
                },
                "message": "Role Listing already exists."
            }
        ), 400
    else:
        try:
            db.session.add(role_listing)
            db.session.commit()
        except:
            return jsonify(
                {
                    "code": 500,
                    "data": {
                        "role_listing": role_listing.json()
                    },
                    "message": "An error occurred creating the role_listing."
                }
            ), 500
        return jsonify(
            {
                "code": 201,
                "data": role_listing.json()
            }
        ), 201



# Updates a role_listing
# Sample input:
# {
#     "Role_Listing_ID": 4,
#     "Role_Listing_Desc": "This is a test role listing.",
#     "Role_Listing_Source": 1,
#     "Role_Listing_Close": "2021-01-01",
#     "Role_Listing_Updater": 2
# }
@app.route("/role_listing/update", methods=['PUT'])
def update_role_listing():
    data = request.get_json()
    listing_id = data['Role_Listing_ID']
    role_listing = Role_Listing.query.filter_by(Role_Listing_ID=listing_id).first()
    if role_listing:
        try:
            role_listing.Role_Listing_Desc = data['Role_Listing_Desc']
            role_listing.Role_Listing_Source = data['Role_Listing_Source']
            role_listing.Role_Listing_Close = data['Role_Listing_Close']
            role_listing.Role_Listing_Updater = data['Role_Listing_Updater']
            role_listing.Role_Listing_ts_update = func.now()
            db.session.commit()
        except:
            return jsonify(
                {
                    "code": 500,
                    "data": {
                        "role_listing": role_listing.json()
                    },
                    "message": "An error occurred updating the role_listing."
                }
            ), 500
        return jsonify(
            {
                "code": 200,
                "data": role_listing.json()
            }
        ), 200
    else:
        return jsonify(
            {
                "code": 404,
                "data": {
                    "listing_id": listing_id
                },
                "message": "Role Listing not found."
            }
        ), 404


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

# Makes a staff member a candidate for a role listing
# Sample Input:
# {
#     "candidate_id" : 1,
#     "role_listing_id" : 1``
# }
@app.route("/role_listing/candidates", methods=['POST'])
def create_candidate():
    data = request.get_json()

    candidate_id = data['candidate_id']
    role_listing_id = data['role_listing_id']

    if (Candidates.query.filter_by(Candidate_ID=candidate_id, Role_Listing_ID=role_listing_id).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "candidate_id": candidate_id,
                    "role_listing_id": role_listing_id
                },
                "message": "Candidate already exists."
            }
        ), 400

    candidate = Candidates(candidate_id, role_listing_id)

    try:
        db.session.add(candidate)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "candidate_id": candidate_id,
                    "role_listing_id": role_listing_id
                },
                "message": "An error occurred creating the candidate."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": candidate.json()
        }
    ), 201

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