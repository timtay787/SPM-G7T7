import unittest
import flask_testing
import json
from sqlalchemy import func
from role_listing import app, db, Role_Listing
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

class TestCreateRoleListing(TestApp):
    maxDiff = None
    def test_create_role_listing(self):
        request_body = {
            'role_listing_id': 1008,
            'role_id': 1,
            'role_listing_desc': 'Manages the sales team.',
            'role_listing_source': 8,
            'role_listing_open': '2023-11-11',
            'role_listing_close': '2023-12-12',
            'role_listing_creator': 1,
        }

        response = self.client.post("/role_listing",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json, {
                "message": "Role Listing created successfully."
            })
        
    def test_create_role_listing_with_existing_role_id_and_role_listing_source(self):
        request_body = {
            'role_listing_id': 1008,
            'role_id': 1,
            'role_listing_desc': 'Manages the sales team.',
            'role_listing_source': 8,
            'role_listing_open': '2023-11-11',
            'role_listing_close': '2023-12-12',
            'role_listing_creator': 1,
        }

        response = self.client.post("/role_listing",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        response = self.client.post("/role_listing",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json, {
                "message": "Role Listing with the same role and hiring manager already exists."
            })
        
    def test_create_role_listing_with_invalid_role_id(self):
        request_body = {
            'role_listing_id': 1008,
            'role_id': 100,
            'role_listing_desc': 'Manages the sales team.',
            'role_listing_source': 8,
            'role_listing_open': '2023-11-11',
            'role_listing_close': '2023-12-12',
            'role_listing_creator': 1,
        }

        response = self.client.post("/role_listing",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json, {
                "message": "An error occurred creating the role_listing."
            })
        
    def test_create_role_listing_with_invalid_staff_id(self):
        request_body = {
            'role_listing_id': 1008,
            'role_id': 1,
            'role_listing_desc': 'Manages the sales team.',
            'role_listing_source': 8,
            'role_listing_open': '2023-11-11',
            'role_listing_close': '2023-12-12',
            'role_listing_creator': 100,
        }

        response = self.client.post("/role_listing",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        self.assertEqual(response.json, {
                "message": "An error occurred creating the role_listing."
            })

if __name__ == "__main__":
    unittest.main()