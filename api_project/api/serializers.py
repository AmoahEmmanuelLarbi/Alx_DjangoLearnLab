from rest_framework import serializers
from .models import Book


# serializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["title", "author"]

    def validate_title(self, value):
        if len(value) < 10:
            raise serializers.ValidationError(
                "Title must not be less than 10 characters long"
            )
        return value
