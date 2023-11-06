from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/sbrp_db'

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
    
class Staff_Roles(db.Model):
    __tablename__ = 'staff_roles'
    staff_id = db.Column(db.Integer, primary_key= True)
    staff_role = db.Column(db.Integer, primary_key= True)
    role_type = db.Column(db.String(20), nullable=False)
    sr_status = db.Column(db.String(20), nullable=False)

    def __init__(self, staff_id, staff_role, role_type, sr_status):
        self.staff_id = staff_id
        self.staff_role = staff_role
        self.role_type = role_type
        self.sr_status = sr_status

    def json(self):
        return {"StaffID": self.staff_id,
                "RoleID": self.staff_role,
                "RoleType": self.role_type,
                "Status": self.sr_status
                }
    
class Staff_Skills(db.Model):
    __tablename__ = 'staff_skill'
    staff_id = db.Column(db.Integer, primary_key= True)
    skill_id = db.Column(db.Integer, primary_key= True)
    ss_status = db.Column(db.String(20), nullable=False)

    def __init__(self, staff_id, skill_id, ss_status):
        self.staff_id = staff_id
        self.skill_id = skill_id
        self.ss_status = ss_status

    def json(self):
        return {"StaffID": self.staff_id,
                "SkillID": self.skill_id,
                "Status": self.ss_status
                }
    
class Staff_RO(db.Model):
    __tablename__ = 'staff_reporting_officer'
    staff_id = db.Column(db.Integer, primary_key= True)
    ro_id = db.Column(db.Integer, primary_key= True)

    def __init__(self, staff_id, ro_id):
        self.staff_id = staff_id
        self.ro_id = ro_id

    def json(self):
        return {"StaffID": self.staff_id,
                "ROID": self.ro_id,
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

# Retrieves every manager in the database
@app.route("/staff/manager")
def get_all_manager():
    stafflist = Staff.query.filter_by(sys_role="manager").all()
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
            "message": "There are no managers."
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

# Retrieves roles that a staff has based on staff_id
@app.route("/staff/role/<int:staff_id>")
def find_roles_by_staff_id(staff_id):
    staff_roles = Staff_Roles.query.filter_by(staff_id=staff_id).all()
    if staff_roles:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "staff_roles": [staff_role.json() for staff_role in staff_roles]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Staff roles not found."
        }
    ), 404

# Retrieves staff's primary role based on staff_id
@app.route("/staff/p_role/<int:staff_id>")
def find_p_role_by_staff_id(staff_id):
    primary_role = Staff_Roles.query.filter_by(staff_id=staff_id, role_type="primary").first()
    if primary_role:
        return jsonify(
            {
                "code": 200,
                "data": primary_role.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Staff's primary role not found."
        }
    ), 404

# Retrieves active skills a staff member has based on staff_id
@app.route("/staff/activeskills/<int:staff_id>")
def find_active_skills_by_staff_id(staff_id):
    staff_skills = Staff_Skills.query.filter_by(staff_id=staff_id, ss_status="active").all()
    if staff_skills:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "staff_skills": [staff_skill.json() for staff_skill in staff_skills]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Staff skills not found."
        }
    ), 404

# Retrieves skills that a staff has based on staff_id
@app.route("/staff/skillsofstaff/<int:staff_id>")
def find_skills_by_staff_id(staff_id):
    staff_skills = Staff_Skills.query.filter_by(staff_id=staff_id).all()
    if staff_skills:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "staff_skills": [staff_skill.json() for staff_skill in staff_skills]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Staff skills not found."
        }
    ), 404

# Retrieves all staff that possess a specific skill based on skill_id
@app.route("/staff/staffwithskill/<int:skill_id>")
def find_staff_by_skill_id(skill_id):
    staff_skills = Staff_Skills.query.filter_by(skill_id=skill_id).all()
    if staff_skills:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "staff_skills": [staff_skill.json() for staff_skill in staff_skills]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "No staff with specified skill found."
        }
    ), 404

# Retrieves the reporting officer of a staff based on staff_id
@app.route("/staff/officerofstaff/<int:staff_id>")
def find_ro_by_staff_id(staff_id):
    staff_ro = Staff_RO.query.filter_by(staff_id=staff_id).first()
    if staff_ro:
        return jsonify(
            {
                "code": 200,
                "data": staff_ro.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Reporting Officer not found."
        }
    ), 404

# Retrieves the staff that report to a reporting officer based on ro_id
@app.route("/staff/staffofofficer/<int:staff_id>")
def find_staff_by_ro_id(staff_id):
    staff_ro = Staff_RO.query.filter_by(ro_id=staff_id).all()
    if staff_ro:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "staff_ro": [staff_ro.json() for staff_ro in staff_ro]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Staff not found."
        }
    ), 404

# Sets the status of a certain skill of a staff member based on staff_id and skill_id
@app.route("/staff/setskillstatus/<int:staff_id>/<int:skill_id>/<ss_status>", methods=['PUT'])
def set_skill_status(staff_id, skill_id, ss_status):
    staff_skill = Staff_Skills.query.filter_by(staff_id=staff_id, skill_id=skill_id).first()
    if staff_skill:
        if ss_status not in ['active', 'unverified', 'in-progress']:
            return jsonify(
                {
                    "code": 400,
                    "data": {
                        "staff_id": staff_id,
                        "skill_id": skill_id,
                        "ss_status": ss_status
                    },
                    "message": "Invalid status."
                }
            ), 400
        else:
            staff_skill.ss_status = ss_status
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": staff_skill.json()
                }
            )
    return jsonify(
        {
            "code": 404,
            "data": {
                "staff_id": staff_id,
                "skill_id": skill_id,
                "ss_status": ss_status
            },
            "message": "Staff skill not found."
        }
    )


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
