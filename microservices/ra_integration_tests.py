import unittest
import flask_testing
import json
from sqlalchemy import func
from role_application import app, db, Role_Application
from datetime import datetime

def clear_data(session):
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        session.execute(table.delete())
    session.commit()

class TestApp(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True
    
    def create_app(self):
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        clear_data(db.session)

class TestCreateApplication(TestApp):
    maxDiff = None
    def test_create_application(self):
        request_body = {
            'role_listing_id': 2008,
            'staff_id': 4,
            'reason_for_application': 'I am interested in this role.'
        }

        response = self.client.post("/role_application",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json, {
                "message": "Application created successfully."
            })
        
    def test_create_application_with_existing_role_listing_id_and_staff_id(self):
        request_body = {
            'role_listing_id': 2008,
            'staff_id': 4,
            'reason_for_application': 'I am interested in this role.'
        }

        response = self.client.post("/role_application",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        response = self.client.post("/role_application",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json, {
                "message": "You have already applied for this role."
            })
    def test_create_applicaton_with_invalid_role_listing_id(self):
        request_body = {
            'role_listing_id': 2009,
            'staff_id': 4,
            'reason_for_application': 'I am interested in this role.'
        }
        response = self.client.post("/role_application",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json, {
                "message": "An error occurred creating the application."
            })
        
    def test_create_application_with_invalid_staff_id(self):
        request_body = {
            'role_listing_id': 2008,
            'staff_id': 100,
            'reason_for_application': 'I am interested in this role.'
        }
        response = self.client.post("/role_application",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json, {
                "message": "An error occurred creating the application."
            })


if __name__ == "__main__":
    unittest.main()