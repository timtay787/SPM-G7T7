from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/skill_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app) 


class Skill(db.Model):
    __tablename__ = 'skill_details'
    skill_id = db.Column(db.Integer, primary_key= True)
    skill_name = db.Column(db.String(50), nullable=False)
    skill_status = db.Column(db.String(20), nullable=False)

    def __init__(self, skill_id, skill_name, skill_status):
        self.skill_id = skill_id
        self.skill_name = skill_name
        self.skill_status = skill_status

    def json(self):
        return {"SkillID": self.skill_id,
                "SkillName": self.skill_name,
                "SkillStatus": self.skill_status
                }

# Retrieves every skill in the database
@app.route("/skill")
def get_all_skill():
    skilllist = Skill.query.all()
    if len(skilllist):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "skill": [skill.json() for skill in skilllist]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no skills."
        }
    ), 404

# Retrieves an active skill based on skill_id
@app.route("/skill/<int:skill_id>")
def find_by_skill_id(skill_id):
    skill = Skill.query.filter_by(skill_id=skill_id).first()
    if skill:
        if skill.skill_status == 'active':
            return jsonify(
                {
                    "code": 200,
                    "data": skill.json()
                }
            )
        else:
            return jsonify(
                {
                    "code": 404,
                    "message": "Skill inactive."
                }
            ), 404
    return jsonify(
        {
            "code": 404,
            "message": "Skill not found."
        }
    ), 404

# Retrieves a skill based on skill_id
@app.route("/skill/anystatus/<int:skill_id>")
def find_anyskill_by_skill_id(skill_id):
    skill = Skill.query.filter_by(skill_id=skill_id).first()
    if skill:
        return jsonify(
            {
                "code": 200,
                "data": skill.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Skill not found."
        }
    ), 404

# Sets the status of a skill based on skill_id
@app.route("/skill/setstatus/<int:skill_id>/<status>", methods=['PUT'])
def update_skill_status(skill_id, status):
    skill = Skill.query.filter_by(skill_id=skill_id).first()
    if skill:
        if status not in ['active', 'inactive']:
            return jsonify(
                {
                    "code": 400,
                    "data": {
                        "skill_id": skill_id,
                        "status": status
                    },
                    "message": "Invalid status."
                }
            ), 400
        else:
            skill.skill_status = status
            db.session.commit()
            return jsonify(
                {
                    "code": 200,
                    "data": skill.json()
                }
            )
    return jsonify(
        {
            "code": 404,
            "data": {
                "skill_id": skill_id
            },
            "message": "Skill not found."
        }
    ), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5002,debug=True)