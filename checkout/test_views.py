from django.test import TestCase


class TestView(TestCase):

    def test_cache_checkout_data(self):  # nope
        response = self.client.get('/checkout/cache_checkout_data/')
        self.assertEqual(response.status_code, 200)

    def test_checkout(self):  # nope
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

    def test_checkout_success(self):  # nope
        response = self.client.get('/checkout/checkout_success/<order_number>')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
