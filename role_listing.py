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
    role_listing_id = db.Column(db.Integer, primary_key= True)
    role_id = db.Column(db.Integer, nullable=False)
    role_listing_desc = db.Column(db.String(50000), nullable=False)
    role_listing_source = db.Column(db.Integer, nullable=False)
    role_listing_open = db.Column(db.Date, nullable=False)
    role_listing_close = db.Column(db.Date, nullable=False)
    role_listing_creator = db.Column(db.Integer, nullable=False)
    role_listing_ts_create = db.Column(db.DateTime, nullable=False)
    # country = db.Column(db.String(50), nullable=False)
    # career_Level = db.Column(db.String(50), nullable=False)
    role_listing_updater = db.Column(db.Integer, nullable=False)
    role_listing_ts_update = db.Column(db.DateTime, nullable=False)

    def __init__(self, role_listing_id, role_id, role_listing_desc, role_listing_source, role_listing_open, role_listing_close, role_listing_creator, role_listing_ts_create, role_listing_updater, role_listing_ts_update):
        self.role_listing_id = role_listing_id
        self.role_id = role_id
        self.role_listing_desc = role_listing_desc
        self.role_listing_source = role_listing_source
        self.role_listing_open = role_listing_open
        self.role_listing_close = role_listing_close
        self.role_listing_creator = role_listing_creator
        self.role_listing_ts_create = role_listing_ts_create
        # self.country = country
        self.role_listing_updater = role_listing_updater
        self.role_listing_ts_update = role_listing_ts_update


    def json(self):
        return {"RoleListingID": self.role_listing_id,
                "RoleID": self.role_id,
                "RoleListingDescription": self.role_listing_desc,
                "RoleListingSource": self.role_listing_source,
                "RoleListingOpen": self.role_listing_open,
                "RoleListingClose": self.role_listing_close,
                "RoleListingCreator": self.role_listing_creator,
                "RoleListingTimestampCreate": self.role_listing_ts_create,
                # "Country": self.country,
                # "CareerLevel": self.career_level,
                "RoleListingUpdater": self.role_listing_updater,
                "RoleListingTimestampUpdate": self.role_listing_ts_update
                }

class Candidates(db.Model):
    __tablename__ = 'candidates'
    candidate_id = db.Column(db.Integer, primary_key= True)
    role_listing_id = db.Column(db.Integer, primary_key= True)

    def __init__(self, candidate_id, role_listing_id):
        self.candidate_id = candidate_id
        self.role_listing_id = role_listing_id
    
    def json(self):
        return {"CandidateID": self.candidate_id,
                "RoleListingID": self.role_listing_id
                }
    
# Creates a new role_listing
# Sample input:
# {
#     "role_lsting_id": 4,
#     "role_id": 1,
#     "role_listing_desc": "This is a test role listing.",
#     "role_listing_source": 1,
#     "role_listing_open": "2021-01-01",
#     "role_listing_close": "2021-01-02",
#     "role_listing_creator": 2
# }
@app.route("/role_listing", methods=['POST'])
def create_role_listing():
    data = request.get_json()
    
    role_listing = Role_Listing(data["role_listing_id"], data["role_id"], data["role_listing_desc"], data["role_listing_source"], data["role_listing_open"], data["role_listing_close"], data["role_listing_creator"], func.now(), 0, '')
    role_listing_check = Role_Listing.query.filter_by(role_listing_id=data["role_listing_id"]).first()
    if role_listing_check:
        return jsonify(
            {
                "code": 400,
                "data": {
                    "role_listing": role_listing_check.json()
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
                "code": 202,
                "data": role_listing.json(),
                "message": "Role Listing created successfully."
            }
        ), 201



# Updates a role_listing
# Sample input:
# {
#     "role_listing_id": 4,
#     "role_listing_desc": "This is a test role listing.",
#     "role_listing_source": 1,
#     "role_listing_open": "2021-01-01",
#     "role_listing_close": "2021-01-02",
#     "role_listing_updater": 2
# }
@app.route("/role_listing/update", methods=['PUT'])
def update_role_listing():
    data = request.get_json()
    current_datetime = datetime.now()
    listing_id = data['role_listing_id']
    role_listing = Role_Listing.query.filter_by(role_listing_id=listing_id).first()
    if role_listing:
        try:
            role_listing.role_listing_desc = data['role_listing_desc']
            role_listing.role_listing_source = data['role_listing_source']
            role_listing.role_listing_open = data['role_listing_open']
            role_listing.role_listing_close = data['role_listing_close']
            role_listing.role_listing_updater = data['role_listing_updater']
            role_listing.role_listing_ts_update = current_datetime
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
                "data": role_listing.json(),
                "message": "Role Listing updated successfully."
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
    role_listing = Role_Listing.query.filter_by(role_listing_id=listing_id).first()
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
    role_listing = Role_Listing.query.filter_by(role_id=role_id).all()
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

    if (Candidates.query.filter_by(candidate_id=candidate_id, role_listing_id=role_listing_id).first()):
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
    candidates = Candidates.query.filter_by(role_listing_id=role_listing_id).all()
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
    candidate = Candidates.query.filter_by(candidate_id=candidate_id, role_listing_id=role_listing_id).first()
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