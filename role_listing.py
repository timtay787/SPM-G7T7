from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/role_listing_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app) 


class Role_Listing(db.Model):
    __tablename__ = 'role_listing'
    listing_id = db.Column(db.Integer, primary_key= True)
    role_id = db.Column(db.Integer, nullable=False)
    dept = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    closing_date = db.Column(db.DateTime, nullable=False)
    career_level = db.Column(db.String(50), nullable=False)
    hiring_manager_id = db.Column(db.Integer, nullable=False)
    responsibilities = db.Column(db.String(50000), nullable=False)

    def __init__(self, listing_id, role_id, dept, country, closing_date, career_level, hiring_manager_id, responsibilities):
        self.listing_id = listing_id
        self.role_id = role_id
        self.dept = dept
        self.country = country
        self.closing_date = closing_date
        self.career_level = career_level
        self.hiring_manager_id = hiring_manager_id
        self.responsibilities = responsibilities

    def json(self):
        return {"ListingID": self.listing_id,
                "RoleID": self.role_id,
                "Department": self.dept,
                "Country": self.country,
                "ClosingDate": self.closing_date,
                "CareerLevel": self.career_level,
                "HiringManagerID": self.hiring_manager_id,
                "Responsibilities": self.responsibilities
                }

# Retrieves every role_listing in the database
@app.route("/role_listing")
def get_all_role_listing():
    role_listing_list = Role_Listing.query.all()
    if len(role_listing_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "role_listing": [role_listing.json() for role_listing in role_listing_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no role_listing."
        }
    ), 404

# Retrieves a role_listing based on listing_id
@app.route("/role_listing/<int:listing_id>")
def find_by_listing_id(listing_id):
    role_listing = Role_Listing.query.filter_by(listing_id=listing_id).first()
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
    role_listing_list = Role_Listing.query.filter_by(role_id=role_id).all()
    if len(role_listing_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "role_listing": [role_listing.json() for role_listing in role_listing_list]
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