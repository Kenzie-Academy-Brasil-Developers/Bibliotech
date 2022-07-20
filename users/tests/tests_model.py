import email
from sqlite3 import IntegrityError
from django.test import TestCase
from traitlets import default
from users.models import User

class UserTest(TestCase):
   @classmethod
   def setUpTestData(cls):
      print()
      print("Executando setUpTestData")

      cls.user1 = User.objects.create(
         email="teste@gmail.com",
         password="1234",
         full_name="Fulano da Silva Pereira dos Testes",
         username="testando123testando",
         birth_date="2001-01-01",
         phone="12 993567947",
         is_debt=False
      )

      cls.user2 = User.objects.create(
         email="teste@gmail.com",
         password="1234",
         full_name="Fulano da Silva Pereira dos Testes",
         username="testando123testando",
         birth_date="2001-01-01",
         phone="123456789101112",
         is_debt=False
      )


   def test_model_user_max_length(self):
      print("Executando test_model_user_max_length")
      user = User.objects.get(id=1)

      max_length_name = user._meta.get_field("full_name").max_length
      max_length_phone = user._meta.get_field("phone").max_length
      max_length_email = user._meta.get_field("email").max_length
      
      self.assertEqual(max_length_name, 70)
      self.assertEqual(max_length_phone, 12)
      self.assertEqual(max_length_email, 255)

   
   def test_mode_user(self):
      print("Executando test_model_user")
      user = User.objects.get(id=1)

      unique_email = user._meta.get_field("email").unique
      default_is_debt = user._meta.get_field("is_debt").default
      null_is_debt = user._meta.get_field("is_debt").null
      auto_now_add_created = user._meta.get_field("created_at").auto_now_add
   
      self.assertEqual(unique_email, True)
      self.assertEqual(default_is_debt, False)
      self.assertEqual(null_is_debt, True)
      self.assertEqual(auto_now_add_created, True)

   

   



   

   


