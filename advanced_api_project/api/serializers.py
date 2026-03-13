from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone


# book serializer
class BookSerializer(serializers.ModelSerializer):

    # custom fiel
    date_since_published = serializers.SerializerMethodField

    class Meta:
        model = Book
        fields = "__all__"

        # validate book
        def title_validate(self, value):
            if len(value) < 10:
                raise serializers.ValidationError(
                    "Book title can't be less than 10 characters!"
                )

        def validate(self, data):
            current_date = timezone.now().date()
            if data["publication_date"] > current_date:
                raise serializers.ValidationError(
                    "Publication date can't be in the future!"
                )

        # get value of custom field
        def get_date_since_published(self, obj):
            days = obj.publication_year - timezone.now().date


# author serializer
class AuthorSerializer(serializers.ModelSerializer):

    # nested serializer
    book = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["name", "book"]

        # validate author name
        def name_validate(self, value):
            if len(value) < 10:
                raise serializers.ValidationError(
                    "Author name can't be less than 10 characters"
                )

            if any(char.isdigit() for char in value):
                raise serializers.ValidationError(
                    "Author name can't contain a number or integer!"
                )
