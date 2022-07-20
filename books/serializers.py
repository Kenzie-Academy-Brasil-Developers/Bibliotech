from rest_framework import serializers
from books.models import Book
from genres.serializers import GenreSerializer
from genres.models import Genre
import ipdb


class BookSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, null=True)
    class Meta:
        model = Book
        fields = ["id", "title", "pages", "author", "classification", "genre"]



    def create(self, validated_data):
        genres_characteristic = validated_data.pop("genre")

        book = Book.objects.create(**validated_data)

        for x in genres_characteristic:
            genre = Genre.objects.get_or_create(**x)
            book.genre.add(genre[0])

        return book