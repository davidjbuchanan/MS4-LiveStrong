from django.test import TestCase


class TestView(TestCase):

    def test_add_coupon(self):
        response = self.client.get('/coupons/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'coupons/add_coupon.html')
