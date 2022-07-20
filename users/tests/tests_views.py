from turtle import update
from rest_framework.test import APITestCase
from rest_framework.views import status
from users.models import User
from rest_framework.authtoken.models import Token

class TestUserView(APITestCase):
    @classmethod
    def setUp(self):
        print()
        print("Executando setUp")

        self.user = {
            "email": "teste@gmail.com",
            "password": "1234",
            "full_name": "Fulano da Silva Pereira dos Testes",
            "username": "testando123testando",
            "birth_date": "2001-01-01",
            "phone": "12 993567947",
            "is_debt": False
        }

        self.update = {
            "email": "updateteste@gmail.com",
            "password": "senhaforte",
            "full_name": "Fulano da Silva Pereira dos Testes Atualizados",
            "username": "testando123testando123",
            "birth_date": "2001-01-01",
            "phone": "12 983567847",
            "is_debt": True,
            "created_at": "2021-09-09"
        }


    def test_create_user(self):
        print("Executando test_create_user")
        res = self.client.post('/api/user/signup/', data=self.user)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertNotIn("password", res.data)

    
    def test_user_login(self):
        print("Executando test_user_login")
        user = User.objects.create_user(**self.user)
        res = self.client.post('/api/user/signin/', data={"email": "teste@gmail.com", "password": "1234"})

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn("token", res.data)

    
    def test_user_retrieve(self):
        print("Executando test_user_retrieve")
        user = User.objects.create_user(**self.user)
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        res = self.client.get(f'/api/user/{1}/')

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertNotIn("password", res.data)
        self.assertEqual(res.data['email'], self.user["email"])
        self.assertEqual(res.data['full_name'], self.user["full_name"])
        self.assertEqual(res.data['username'], self.user["username"])
        self.assertEqual(res.data['birth_date'], self.user["birth_date"])
        self.assertEqual(res.data['phone'], self.user["phone"])
        self.assertEqual(res.data['is_debt'], self.user["is_debt"])


    def test_user_update(self):
        print("Executando test_user_update")
        user = User.objects.create_user(**self.user)
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        res = self.client.patch(f'/api/user/{1}/', data=self.update)
        print("res:", res.data)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertNotIn("password", res.data)
        self.assertEqual(res.data['email'], self.update["email"])
        self.assertEqual(res.data['full_name'], self.update["full_name"])
        self.assertEqual(res.data['username'], self.update["username"])
        self.assertEqual(res.data['phone'], self.update["phone"])
        self.assertEqual(res.data['is_debt'], self.update["is_debt"])

    
    def test_user_delete(self):
        print("Executando test_user_delete")
        user = User.objects.create_user(**self.user)
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        res = self.client.delete(f'/api/user/{1}/')

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
  

