import unittest
import flask_testing
import json
from sqlalchemy import func
# from staff import app as staff_app, db as staff_db, Staff, Staff_Roles, Staff_Skills, Staff_RO
# from role import app as role_app, db as role_db, Role, Role_Skills
# from skill import app as skill_app, db as skill_db, Skill
from role_listing import app, db, Role_Listing
# from role_application import app as ra_app, db as ra_db, Role_Application
from datetime import datetime

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
        db.drop_all()

class TestCreateRoleListing(TestApp):
    maxDiff = None
    def test_create_role_listing(self):
        current_time = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
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
        #         "code": 202,
        #         "data": {
        #             "role_listing": {
        #                 'RoleListingID': '1008',
        #                 'RoleID': 1,
        #                 'RoleListingDescription': 'Manages the sales team.',
        #                 'RoleListingSource': 8,
        #                 'RoleListingOpen': '2023-11-11',
        #                 'RoleListingClose': '2023-12-12',
        #                 'RoleListingCreator': 1,
        #                 'RoleListingTimestampCreate': current_time,
        #                 'RoleListingUpdater': None,
        #                 'RoleListingTimestampUpdate': None
        # }
        #         },
                "message": "Role Listing created successfully."
            })


if __name__ == "__main__":
    unittest.main()