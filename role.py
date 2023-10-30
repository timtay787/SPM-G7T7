from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/role_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app) 


class Role(db.Model):
    __tablename__ = 'role_details'
    role_id = db.Column(db.Integer, primary_key= True)
    role_name = db.Column(db.String(50), nullable=False)
    role_desc = db.Column(db.String(50000), nullable=False)
    role_status = db.Column(db.String(20), nullable=False)

    def __init__(self, role_id, role_name, role_desc, role_status):
        self.role_id = role_id
        self.role_name = role_name
        self.role_desc = role_desc
        self.role_status = role_status

    def json(self):
        return {"RoleID": self.role_id,
                "RoleName": self.role_name,
                "RoleDescription": self.role_desc,
                "RoleStatus": self.role_status
                }
    
class Role_Skills(db.Model):
    __tablename__ = 'role_skill'
    role_id = db.Column(db.Integer, primary_key= True)
    skill_id = db.Column(db.Integer, primary_key= True)

    def __init__(self, role_id, skill_id):
        self.role_id = role_id
        self.skill_id = skill_id

    def json(self):
        return {"RoleID": self.role_id,
                "SkillID": self.skill_id
                }

# Retrieves every active role in the database
@app.route("/role")
def get_all_role():
    rolelist = Role.query.filter_by(role_status="Active").all()
    if len(rolelist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "role": [role.json() for role in rolelist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no roles."
        }
    ), 404

# Retrieves a role based on role_id
@app.route("/role/<int:role_id>")
def find_by_role_id(role_id):
    role = Role.query.filter_by(role_id=role_id).first()
    if role:
        return jsonify(
            {
                "code": 200,
                "data": role.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Role not found."
        }
    ), 404

# Retrieves skills that a role requires based on role_id
@app.route("/role/skill/<int:role_id>")
def find_skills_by_role_id(role_id):
    role_skill_list = Role_Skills.query.filter_by(role_id=role_id).all()
    if len(role_skill_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "role_skill": [role_skill.json() for role_skill in role_skill_list]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Role Skill not found."
        }
    ), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001,debug=True)
