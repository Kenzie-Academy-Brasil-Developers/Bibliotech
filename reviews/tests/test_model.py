from django.db import IntegrityError
from django.forms import ValidationError
from django.test import TestCase
from books.models import Book
from genres.models import Genre
from users.models import User
from ..models import Review

class ReviewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.valid_stars = 5
        cls.min_fail_stars = -1
        cls.max_fail_stars = 11
        cls.valid_type_review =  "Critique"
        cls.invalid_type_review = "invalid review_type"
        cls.review_field = "sample text"
        cls.recommendation = "rec"

        cls.genre = Genre.objects.create(name="test genre")
        cls.user = User.objects.create_user(email="test@mail.com", password="1234", birth_date='1999-01-01')
        cls.book = Book.objects.create(title="test book", pages=100, author="Test", classification=5)
        cls.book.genre.add(cls.genre)
        
        cls.review_1 = Review.objects.create(stars=cls.valid_stars, recommendation=cls.recommendation, review=cls.review_field, type_review=cls.valid_type_review, user=cls.user, book=cls.book)
        cls.review_2 = Review.objects.create(stars=cls.valid_stars, recommendation=cls.recommendation, review=cls.review_field, type_review=cls.valid_type_review, user=cls.user, book=cls.book)

    def test_stars_value_success(self):
        self.assertEqual(self.review_1.stars, self.valid_stars)
    
    def test_stars_max_value_fail(self):
        with self.assertRaises(ValidationError):
            review = Review.objects.create(stars=self.max_fail_stars, recommendation=self.recommendation, review=self.review_field, type_review=self.valid_type_review, user=self.user, book=self.book)
            review.full_clean()
    
    def test_stars_min_value_fail(self):
        with self.assertRaises(ValidationError):
            review = Review.objects.create(stars=self.min_fail_stars, recommendation=self.recommendation, review=self.review_field, type_review=self.valid_type_review, user=self.user, book=self.book)
            review.full_clean()
    
    def test_review_field_value(self):
        self.assertEqual(self.review_1.review, self.review_field)
    
    def test_recommendation_max_length(self):
        max_length = self.review_1._meta.get_field("recommendation").max_length
        self.assertEqual(max_length, 50)
    
    def test_type_review_valid_value(self):
        self.assertEqual(self.review_1.type_review, self.valid_type_review)
    
    def test_type_review_invalid_value(self):
        with self.assertRaises(ValidationError):
            review = Review.objects.create(stars=self.valid_stars, recommendation=self.recommendation, review=self.review_field, type_review=self.invalid_type_review, user=self.user, book=self.book)
            review.full_clean()
    
    def test_user_may_have_multiple_reviews(self):
        self.assertEqual(len(self.user.reviews.all()), 2)

    def test_movie_may_have_multiple_reviews(self):
        self.assertEqual(len(self.book.reviews.all()), 2)
    
    def test_review_creation_without_user(self):
        with self.assertRaises(IntegrityError):
            review = Review.objects.create(stars=self.valid_stars, recommendation=self.recommendation, review=self.review_field, type_review=self.valid_type_review, book=self.book)
    
    def test_review_creation_without_book(self):
        with self.assertRaises(IntegrityError):
            review = Review.objects.create(stars=self.valid_stars, recommendation=self.recommendation, review=self.review_field, type_review=self.valid_type_review, user=self.user)