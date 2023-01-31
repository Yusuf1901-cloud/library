from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Book

class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.book = Book.objects.create(
            title="Django for APIs",
            subtitle="Build web APIs with Python and Django",
            author="William S. Vincent",
            isbn="9781735467221",
        )
        return super().setUpTestData()
    
    def test_api_listView(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book)

