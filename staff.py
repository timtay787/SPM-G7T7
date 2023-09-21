from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/sbrp_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app) 

class Staff(db.Model):
    __tablename__ = 'staff_details'
    staff_id = db.Column(db.Integer, primary_key= True)
    staff_fname = db.Column(db.String(50), nullable=False)
    staff_lname = db.Column(db.String(50), nullable=False)
    dept = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    biz_address = db.Column(db.String(255), nullable=False)
    sys_role = db.Column(db.String(20), nullable=False)
    

    def __init__(self, staff_id, staff_fname, staff_lname, dept, email, phone, biz_address, sys_role):
        self.staff_id = staff_id
        self.staff_fname = staff_fname
        self.staff_lname = staff_lname
        self.dept = dept
        self.email = email
        self.phone = phone
        self.biz_address = biz_address
        self.sys_role = sys_role
        

    def json(self):
        return {"StaffID": self.staff_id,
                "StaffFirstName": self.staff_fname,
                "StaffLastName": self.staff_lname,
                "Department": self.dept,
                "Email": self.email,
                "Phone": self.phone,
                "BusinessAddress": self.biz_address,
                "SystemRole": self.sys_role
                }
    
# Retrieves every staff in the database
@app.route("/staff")
def get_all_staff():
    stafflist = Staff.query.all()
    if len(stafflist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "staff": [staff.json() for staff in stafflist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no staff."
        }
    ), 404

# Retrieves a staff based on staff_id
@app.route("/staff/<int:staff_id>")
def find_by_staff_id(staff_id):
    staff = Staff.query.filter_by(staff_id=staff_id).first()
    if staff:
        return jsonify(
            {
                "code": 200,
                "data": staff.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Staff not found."
        }
    ), 404
        

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
