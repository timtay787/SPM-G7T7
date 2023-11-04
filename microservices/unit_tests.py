import unittest
from staff import Staff, Staff_Roles, Staff_Skills, Staff_RO
from role import Role, Role_Skills
from skill import Skill
from role_listing import Role_Listing
from role_application import Role_Application

class TestStaff(unittest.TestCase):
    def test_json(self):
        s1 = Staff(staff_id=1, staff_fname='Jacob', staff_lname='Scott', dept='Sales',
                   email='jacobscott@gmail.com', phone='+65 1234 5678',
                   biz_address='81 VICTORIA STREET,SINGAPORE 123456', sys_role='staff')
        self.assertEqual(s1.json(), {
            'StaffID' : 1,
            'StaffFirstName' : 'Jacob',
            'StaffLastName' : 'Scott',
            'Department' : 'Sales',
            'Email' : 'jacobscott@gmail.com',
            'Phone' : '+65 1234 5678',
            'BusinessAddress' : '81 VICTORIA STREET, SINGAPORE 123456',
            'SystemRole' : 'staff'}
        )   

class TestStaff_Roles(unittest.TestCase):
    def test_json(self):
        sr1 = Staff_Roles(staff_id=1, staff_role=1, role_type='primary', sr_status='active')
        self.assertEqual(sr1.json(), {
            'StaffID' : 1,
            'RoleID' : 1,
            'RoleType' : 'primary',
            'Status' : 'active'}
        )

class TestStaff_Skills(unittest.TestCase):
    def test_json(self):
        ss1 = Staff_Skills(staff_id=1, skill_id=1, ss_status='active')
        self.assertEqual(ss1.json(), {
            'StaffID' : 1,
            'SkillID' : 1,
            'Status' : 'active'}
        )

class TestStaff_RO(unittest.TestCase):
    def test_json(self):
        sro1 = Staff_RO(staff_id=1, ro_id=8)
        self.assertEqual(sro1.json(), {
            'StaffID' : 1,
            'ROID' : 8}
        )

class TestRole(unittest.TestCase):
    def test_json(self):
        r1 = Role(role_id=1, role_name='Sales Manager', role_desc='Manages the sales team.',
                  role_status='active')
        self.assertEqual(r1.json(), {
            'RoleID' : 1,
            'RoleName' : 'Sales Manager',
            'RoleDescription' : 'Manages the sales team.',
            'RoleStatus' : 'active'}
        )

class TestRole_Skills(unittest.TestCase):
    def test_json(self):
        rs1 = Role_Skills(role_id=1, skill_id=7)
        self.assertEqual(rs1.json(), {
            'RoleID' : 1,
            'SkillID' : 7}
        )

class TestSkill(unittest.TestCase):
    def test_json(self):
        s1 = Skill(skill_id=1, skill_name='Python', skill_status='active')
        self.assertEqual(s1.json(), {
            'SkillID' : 1,
            'SkillName' : 'Python',
            'SkillStatus' : 'active'}
        )

class TestRole_Listing(unittest.TestCase):
    def test_json(self):
        rl1 = Role_Listing(role_listing_id=2006, role_id=1, role_listing_desc='This is a test role listing.',
                           role_listing_source=1, role_listing_open='2021-11-01',
                           role_listing_close='2021-11-30', role_listing_creator=1,
                           role_listing_ts_create='2021-10-01 00:00:00', role_listing_updater=1,
                           role_listing_ts_update='2021-10-01 00:00:00')
        self.assertEqual(rl1.json(), {
            'RoleListingID' : 2006,
            'RoleID' : 1,
            'RoleListingDescription' : 'This is a test role listing.',
            'RoleListingSource' : 1,
            'RoleListingOpen' : '2021-11-01',
            'RoleListingClose' : '2021-11-30',
            'RoleListingCreator' : 1,
            'RoleListingTimestampCreate' : '2021-10-01 00:00:00',
            'RoleListingUpdater' : 1,
            'RoleListingTimestampUpdate' : '2021-10-01 00:00:00'}
        )

class TestRole_Application(unittest.TestCase):
    def test_json(self):
        ra1 = Role_Application(role_listing_id=2006, staff_id=1, role_app_status='active',
                               role_app_ts_create='2021-10-01 00:00:00',
                               reason_for_application='I am interested in this role.')
        self.assertEqual(ra1.json(), {
            'RoleApplicationID' : None,
            'RoleListingID' : 2006,
            'StaffID' : 1,
            'RoleApplicationStatus' : 'active',
            'RoleApplicationTimestampCreate' : '2021-10-01 00:00:00',
            'ReasonForApplication' : 'I am interested in this role.'}
        )

if __name__ == "__main__":
    unittest.main()