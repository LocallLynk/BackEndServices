import unittest
from faker import Faker
from app import create_app
from database import db
from unittest.mock import patch

class TestNeighbor(unittest.TestCase):
    def setUp(self):
        app = create_app('TestingConfig')
        with app.app_context():
            db.create_all()
        self.app = app.test_client()

    def test_create_neighbor(self):
        fake = Faker()
        first_name = fake.first_name()
        last_name = fake.last_name()
        phone = fake.phone_number()
        email = fake.email()
        zipcode = fake.zipcode()
        username = fake.user_name()
        password = fake.password()
        admin = 1

        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "email": email,
            "zipcode": zipcode,
            "username": username,
            "password": password,
            "admin": admin
        }

        response = self.app.post('/neighbor/', json=payload)
        self.assertEqual(response.status_code, 201)

    @patch('controllers.neighborController.NeighborService.get_all')
    def test_get_all_neighbors(self):
        response = self.app.get('/neighbor/')
        self.assertEqual(response.status_code, 200)


        

if __name__ == '__main__':
    unittest.main()