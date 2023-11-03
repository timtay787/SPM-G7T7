from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_cors import CORS
from datetime import datetime
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/role_listing_db'
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
    current_datetime = datetime.now()
    role_listing = Role_Listing(data["role_listing_id"], data["role_id"], data["role_listing_desc"], data["role_listing_source"], data["role_listing_open"], data["role_listing_close"], data["role_listing_creator"], current_datetime, 0, '')
    #check if existing role listing has the same role_id and role_listing_source
    role_listing_check = Role_Listing.query.filter_by(role_id=data["role_id"], role_listing_source=data["role_listing_source"] ).first()
    if role_listing_check:
        return jsonify(
            {
                "code": 400,
                "data": {
                    "role_listing": role_listing_check.json()
                },
                "message": "Role Listing with the same role and hiring manager already exists."
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
        role_listing_check = Role_Listing.query.filter_by(role_listing_id=data["role_listing_id_new"]).first()
        if role_listing_check and (role_listing.role_listing_id != data["role_listing_id_new"]):
            return jsonify(
                {
                    "code": 405,
                    "data": {
                        "listing_id": listing_id
                    },
                    "message": "Role Listing with the same role and hiring manager already exists."
                }
            ), 405
        else:
            try:
                role_listing.role_listing_id = data['role_listing_id_new']
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

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5003,debug=True)