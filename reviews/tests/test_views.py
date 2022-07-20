from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework.views import status
from books.models import Book
from genres.models import Genre
from reviews.models import Review

from users.models import User

class TestReviewView(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.pw = '1234'
        cls.name = 'user user'
        cls.birth_date = '1999-01-01'
        cls.phone = '12345'

        cls.admin_data = {'email': 'admin@mail.com', 'password': cls.pw, 'full_name': 'admin adm', 'username': 'admin', 'birth_date': cls.birth_date, 'phone': cls.phone, 'is_debt': False}
        cls.user_data_1 = {'email': 'user1@mail.com','password': cls.pw,'full_name': cls.name,'username': 'user_1', 'birth_date': cls.birth_date, 'phone': cls.phone, 'is_debt': False}
        cls.user_data_2 = {'email': 'user2@mail.com','password': cls.pw,'full_name': cls.name, 'username': 'user_2', 'birth_date': cls.birth_date, 'phone': cls.phone, 'is_debt': False}      
        cls.update_data = { 'review': 'test update' }

        cls.admin = User.objects.create_superuser(**cls.admin_data)
        cls.user_1 = User.objects.create_user(**cls.user_data_1)
        cls.user_2 = User.objects.create_user(**cls.user_data_2)
        cls.genre = Genre.objects.create(name='genre')
        cls.book = Book.objects.create(title='Test title', pages=100, author='Test author', classification=5)
        cls.book.genre.add(cls.genre)

        cls.admin_token = Token.objects.create(user=cls.admin)
        cls.user_1_token = Token.objects.create(user=cls.user_1)
        cls.user_2_token = Token.objects.create(user=cls.user_2)

        cls.review_data_1 = {'stars': 5, 'review': 'Test rvw', 'recommendation': 'recom', 'type_review': 'Recommendation', 'user': cls.user_1, 'book': cls.book }
        cls.review_data_2 = {'stars': 5, 'review': 'Test rvw', 'recommendation': 'recom', 'type_review': 'Recommendation', 'user': cls.user_2, 'book': cls.book }
        cls.review_1 = Review.objects.create(**cls.review_data_1)
        cls.review_2 = Review.objects.create(**cls.review_data_2)

        cls.unauthorized_msg = 'You do not have permission to perform this action.'
   
    def test_anyone_can_list_reviews_by_book_id(self):
        res = self.client.get(f'/api/book/{self.book.id}/review/')
        self.assertEqual(res.status_code, 200)
    
    def test_reviews_returned_are_only_of_the_corresponding_book_id(self):
        res = self.client.get(f'/api/book/{self.book.id}/review/')
        for rvw in res.data:
            self.assertEqual(rvw['book']['id'], self.book.id)

    def test_only_authenticated_user_can_create_review(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_1_token.key)
        res = self.client.post(f'/api/book/{self.book.id}/review/', data=self.review_data_1)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    
    def test_unauthenticated_user_review_create_fail(self):
        res = self.client.post(f'/api/book/{self.book.id}/review/')
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(str(res.data['detail']), 'Authentication credentials were not provided.')
    
    def test_admin_update_review(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.admin_token.key)
        res = self.client.patch(f'/api/review/{self.review_1.id}/', data=self.update_data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['review'], self.update_data['review'])
    
    def test_owner_update_review(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_1_token.key)
        res = self.client.patch(f'/api/review/{self.review_1.id}/', data=self.update_data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['review'], self.update_data['review'])
    
    def test_owner_update_review_fail(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_2_token.key)
        res = self.client.patch(f'/api/review/{self.review_1.id}/', data=self.update_data)
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(res.data['detail'], self.unauthorized_msg)
    
    def test_admin_delete_review(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.admin_token.key)
        res = self.client.delete(f'/api/review/{self.review_1.id}/')
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_owner_delete_review(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_1_token.key)
        res = self.client.delete(f'/api/review/{self.review_1.id}/')
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_owner_delete_review_fail(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_2_token.key)
        res = self.client.delete(f'/api/review/{self.review_1.id}/')
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(res.data['detail'], self.unauthorized_msg)
        




    

    