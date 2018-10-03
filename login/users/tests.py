from django.test import TestCase
from .models import CustomUser
from rest_framework.test import APITestCase

 # Create your tests here.
class CheckProductAPITest(APITestCase):
    def test_register_user(self):
        # OK is can create
        request_1 = {'password1':'asd123asd123', 'password2':'asd123asd123', 'email': 'teste1@teste.com'}
        response_1 = self.client.post('/api/registration/', request_1)
        self.assertEqual(response_1.status_code, 201)

         # BAD REQUEST email already exist in DB
        request_2 = {'password1':'asd123asd123', 'password2':'asd123asd123', 'email': 'teste1@teste.com'}
        response_2 = self.client.post('/api/registration/', request_2)
        self.assertEqual(response_2.status_code, 400)

          # BAD REQUEST if password1 and password2 does not match
        request_3 = {'password1':'senhacerta', 'password2':'senhaerrada', 'email': 'teste2@teste.com'}
        response_3 = self.client.post('/api/registration/', request_3)
        self.assertEqual(response_3.status_code, 400)

          # BAD REQUEST if password1 does not exist
        request_4 = {'password2':'senhaerrada', 'email': 'teste2@teste.com'}
        response_4 = self.client.post('/api/registration/', request_4)
        self.assertEqual(response_4.status_code, 400)

          # BAD REQUEST if password2 does not exist
        request_5 = {'password1':'senhaerrada', 'email': 'teste2@teste.com'}
        response_5 = self.client.post('/api/registration/', request_5)
        self.assertEqual(response_5.status_code, 400)

          # BAD REQUEST if does not have password field
        request_6 = {'test':'test'}
        response_6 = self.client.post('/api/registration/', request_6)
        self.assertEqual(response_6.status_code, 400)

          # BAD REQUEST if email is not valid
        request_7 = {'password1':'asd123asd123', 'password2':'asd123asd123', 'email': 'teste'}
        response_7 = self.client.post('/api/registration/', request_7)
        self.assertEqual(response_7.status_code, 400)

          # BAD REQUEST if password is less than 8 digits
        request_8 = {'password1':'tem4567', 'password2':'tem4567', 'email': 'teste2@teste.com'}
        response_8 = self.client.post('/api/registration/', request_8)
        self.assertEqual(response_8.status_code, 400)

         # BAD REQUEST if password is too commom
        request_9 = {'password1':'12345678', 'password2':'12345678', 'email': 'teste2@teste.com'}
        response_9 = self.client.post('/api/registration/', request_9)
        self.assertEqual(response_9.status_code, 400)

    def test_create_user(self):
        email_lowercase = 'normal@normal.com'
        user = CustomUser.objects._create_user(email_lowercase, 'teste123')
        self.assertEqual(user.email, email_lowercase)
