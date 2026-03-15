from rest_framework import serializers
from .models import Author, Book
from django.utils import timezone


# book serializer
class BookSerializer(serializers.ModelSerializer):

    # custom fiel
    years_since_published = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ["title", "publication_year", "author", "years_since_published"]
        read_only_fields = ["years_since_published"]

    # validate book
    def validate_title(self, value):
        if len(value) < 10:
            raise serializers.ValidationError(
                "Book title can't be less than 10 characters!"
            )
        return value

    def validate(self, data):
        current_date = timezone.now().date()
        if data["publication_year"] > current_date:
            raise serializers.ValidationError(
                "Publication date can't be in the future!"
            )
        return data

    # get value of custom field
    def get_years_since_published(self, obj):
        current_year = timezone.now().year
        years = current_year - obj.publication_year.year
        return years


# author serializer
class AuthorSerializer(serializers.ModelSerializer):

    # nested serializer
    book = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["name", "book"]

    # validate author name
    def validate_name(self, value):
        if len(value) < 10:
            raise serializers.ValidationError(
                "Author name can't be less than 10 characters"
            )

        if any(char.isdigit() for char in value):
            raise serializers.ValidationError(
                "Author name can't contain a number or integer!"
            )
