from django.test import TestCase
from .models import CustomUser
from rest_framework.test import APITestCase
from .views import get_name
from . import models

 # Create your tests here.
class CheckuserAPITest(APITestCase):
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
        email_1 = 'normal@normal.com'
        user_1 = CustomUser.objects._create_user(email_1, 'teste123')
        self.assertEqual(user_1.email, email_1)

        email_2 = None
        try:
            user_2 = CustomUser.objects._create_user(email_2, 'teste123')
        except:
            self.assertEqual(email_2, None)

    def test_create_superuser(self):
        email_1 = 'normal1@normal.com'
        user_1 = CustomUser.objects.create_superuser(email_1, 'teste123')
        self.assertEqual(user_1.email, email_1)

        email_2 = 'normal2@normal.com'
        try:
            user_2 = CustomUser.objects.create_superuser(email_2, 'teste123', is_staff = False)
        except:
            self.assertEqual(email_2, 'normal2@normal.com')

        email_3 = 'normal3@normal.com'
        try:
            user_3 = CustomUser.objects.create_superuser(email_3, 'teste123', is_superuser = False)
        except:
            self.assertEqual(email_3, 'normal3@normal.com')

    def test_customUser_methods(self):
        email_1 = 'teste1@teste.com'
        user_1 = CustomUser.objects.create_superuser(email_1, 'teste123')
        response_1 = CustomUser.__str__(user_1)
        self.assertEqual(response_1, email_1)

        email_2 = 'teste3@teste.com'
        user_2 = CustomUser.objects.create_superuser(email_2, 'teste123')
        response_2 = CustomUser.get_email(user_2)
        self.assertEqual(response_2, email_2)

class CheckUserAPIViewsTest(APITestCase):
    def test_get_name(self):
        user = {'password1':'asd123asd123', 'password2':'asd123asd123', 'email': 'teste1@teste.com'}
        self.client.post('/api/registration/', user)

        # OK if user exists
        request_1 = {'user_id': '1'}
        response_1 = self.client.post('/api/users/get_name/', request_1)
        self.assertEqual(response_1.status_code, 200)

        # BAD_REQUEST if no user_id in request
        request_2 = {}
        response_2 = self.client.post('/api/users/get_name/', request_2)
        self.assertEqual(response_2.status_code, 400)

        # BAD_REQUEST if user don't exist
        request_3 = {'user_id': '4'}
        response_3 = self.client.post('/api/users/get_name/', request_3)
        self.assertEqual(response_3.status_code, 400)

    def test_update_profile(self):
        user1 = {'password1':'asd123asd123', 'password2':'asd123asd123', 'email': 'teste1@teste.com'}
        user2 = {'password1':'asd123asd123', 'password2':'asd123asd123', 'email': 'teste2@teste.com'}
        self.client.post('/api/registration/', user1)
        self.client.post('/api/registration/', user2)

        # OK if user exists
        request_1 = {'user_id': '1', 'name': 'Test Name', 'email': 'teste3@teste.com', 'photo':'https://i.ytimg.com/vi/pvv1F8iKmMM/maxresdefault.jpg'}
        response_1 = self.client.post('/api/users/update_profile/', request_1)
        self.assertEqual(response_1.status_code, 200)
        self.assertEqual(response_1.json(), {'name':'Test Name', 'email': 'teste3@teste.com', 'photo':'https://i.ytimg.com/vi/pvv1F8iKmMM/maxresdefault.jpg'})

        #  if no user_id in request
        request_2 = {'name': 'Test Name', 'email': 'teste3@teste.com', 'photo':'https://i.ytimg.com/vi/pvv1F8iKmMM/maxresdefault.jpg'}
        response_2 = self.client.post('/api/users/update_profile/', request_2)
        self.assertEqual(response_2.status_code, 400)
        self.assertEqual(response_2.json(), {'error':'Usuário não identificado'})

        #  if no name in request
        request_3 = {'user_id': '1', 'email': 'teste3@teste.com', 'photo':'https://i.ytimg.com/vi/pvv1F8iKmMM/maxresdefault.jpg'}
        response_3 = self.client.post('/api/users/update_profile/', request_3)
        self.assertEqual(response_3.status_code, 200)
        self.assertEqual(response_3.json(), {'name':'unchanged', 'email': 'teste3@teste.com', 'photo': 'https://i.ytimg.com/vi/pvv1F8iKmMM/maxresdefault.jpg'})

        #  if no photo in request
        request_4 = {'user_id': '1', 'name': 'Test Name', 'email': 'teste3@teste.com'}
        response_4 = self.client.post('/api/users/update_profile/', request_4)
        self.assertEqual(response_4.status_code, 200)
        self.assertEqual(response_4.json(), {'name':'Test Name', 'email': 'teste3@teste.com', 'photo':'unchanged'})

        # BAD_REQUEST if email is invalid
        request_5 = {'user_id': '1', 'name': 'Test Name', 'email': 'teste3@testecom', 'photo':'https://i.ytimg.com/vi/pvv1F8iKmMM/maxresdefault.jpg'}
        response_5 = self.client.post('/api/users/update_profile/', request_5)
        self.assertEqual(response_5.status_code, 400)
        self.assertEqual(response_5.json(), {'error':'Email inválido.'})

        # BAD_REQUEST if user don't exist
        request_6 = {'user_id': '4', 'name': 'Test Name', 'email': 'teste3@teste.com', 'photo':'https://i.ytimg.com/vi/pvv1F8iKmMM/maxresdefault.jpg'}
        response_6 = self.client.post('/api/users/update_profile/', request_6)
        self.assertEqual(response_6.status_code, 400)
        self.assertEqual(response_6.json(), {'error': 'Usuário não existe.'})

        # BAD_REQUEST if email exists
        request_7 = {'user_id': '1', 'name': 'Test Name', 'email': 'teste2@teste.com', 'photo':'https://i.ytimg.com/vi/pvv1F8iKmMM/maxresdefault.jpg'}
        response_7 = self.client.post('/api/users/update_profile/', request_7)
        self.assertEqual(response_7.status_code, 400)
        self.assertEqual(response_7.json(), {'error': 'Endereço de email já cadastrado'})

        #  if no email in request
        request_8 = {'user_id': '1', 'name': 'Test Name', 'photo':'https://i.ytimg.com/vi/pvv1F8iKmMM/maxresdefault.jpg'}
        response_8 = self.client.post('/api/users/update_profile/', request_8)
        self.assertEqual(response_8.status_code, 200)
        self.assertEqual(response_8.json(), {'name':'Test Name', 'email': 'unchanged', 'photo':'https://i.ytimg.com/vi/pvv1F8iKmMM/maxresdefault.jpg'})

    def test_get_profile(self):
        user = {'password1':'asd123asd123', 'password2':'asd123asd123', 'email': 'teste1@teste.com'}
        self.client.post('/api/registration/', user)

        # OK if user_id is correct
        request_1 = {'user_id': '1'}
        response_1 = self.client.post('/api/users/get_profile/', request_1)
        self.assertEqual(response_1.status_code, 200)
        self.assertEqual(response_1.json(), {'name': '', 'email': 'teste1@teste.com', 'photo': None})

        # BAD_REQUEST if user_id is not defined
        request_2 = {'user_id': ''}
        response_2 = self.client.post('/api/users/get_profile/', request_2)
        self.assertEqual(response_2.status_code, 400)
        self.assertEqual(response_2.json(), {'error': 'Falha na requisição.'})

        # BAD_REQUEST if user_id is incorrect
        request_3 = {'user_id': '500'}
        response_3 = self.client.post('/api/users/get_profile/', request_3)
        self.assertEqual(response_3.status_code, 400)
        self.assertEqual(response_3.json(), {'error': 'Usuário inválido.'})

        