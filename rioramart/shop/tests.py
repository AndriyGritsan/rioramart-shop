from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from .models import Product, Review

class ReviewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(name="Test product", price=100)

    def test_create_review(self):
        response = self.client.post(
            reverse('add_review', args=[self.product.id]),
            {
                'text': 'Good product',
                'rating': 5
            }
        )

        self.assertEqual(response.status_code, 302)  # редірект
        self.assertEqual(Review.objects.count(), 1)

        review = Review.objects.first()
        self.assertEqual(review.text, 'Good product')
        self.assertEqual(review.rating, 5)