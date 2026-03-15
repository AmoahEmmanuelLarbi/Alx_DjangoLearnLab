from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Author, Book
from django.contrib.auth.models import User
from datetime import date


# writing a test to ensure that Book are created, updated, deleted successfully in the database
# Write tests that simulate API requests and check for correct status codes and response data
class BookAPITestCase(APITestCase):
    # creating data to use for testing
    def setUp(self):
        # create author
        self.author = Author.objects.create(name="Jims Kims")

        # create book
        self.book = Book.objects.create(
            title="Working with REST API",
            publication_year=date(2024, 10, 12),
            author=self.author,
        )

        # create a superuser
        self.user = User.objects.create_superuser(
            username="james", password="james@admin12"
        )

        self.list_url = reverse("books")
        self.create_url = reverse("book-create")
        self.update_url = reverse("book-update", args=[self.book.pk])
        self.delete_url = reverse("book-delete", args=[self.book.pk])

    # test to get data
    def test_get_book(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)

    # test to ensure unathorized user cannot create book
    def test_unauthorized_create_book(self):
        data = {
            "title": "System Design Architecture",
            "publication_year": "2026-1-30",
            "author": "1",
        }
        response = self.client.post(self.create_url, data)
        print("Test: UnAuthorized creating of book")
        # print("Returned status code:", response.status_code)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # print(response.data)

    # test if authorized user can create a book
    def test_authorized_create_book(self):
        # self.client.login(username="james", password="james@admin12")
        self.client.force_authenticate(self.user)
        data = {
            "title": "Django ORM",
            "publication_year": "2024-1-30",
            "author": self.author.pk,
        }
        # print(user)
        print("Test: Authorized creating of book")
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # print(
        #     f"Response code from authorized user: {response.status_code}, Data sent to server: {response.data}"
        # )

    # # test to update book by authorized user
    def test_authorized_update_book(self):
        data = {
            "title": "The Django Playbook",
            "publication_year": "2020-01-10",
            "author": "1",
        }
        self.client.force_authenticate(self.user)
        # self.client.force_login(self.user)
        response = self.client.put(self.update_url, data)
        print("Response code:", response.status_code)
        print("Data:", response.data)
        print("Methods Allowed:", response.headers["Allow"])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # test to updated book by unauthorized user
    def test_unauthorized_update_book(self):
        data = {
            "title": "Version Control with Git",
            "publication_year": "2024-01-10",
            "author": self.author.pk,
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # # test to delete book
    def test_unauthorized_delete_book(self):
        response = self.client.delete(self.delete_url)
        # print("Methods Allowed for delete:", response.headers["Allow"])
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
