from django.test import TestCase
from products.models import Product

class TestView(TestCase):

    def test_view_bag(self): # ok
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_coupon_apply(self):  # ok
        response = self.client.get('/bag/apply/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_to_bag(self):  # not working
        item = Product.objects.create(name='test', price='10', description='testdetail')
        response = self.client.get(f'/bag/add/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    # def test_adjust_bag(self):
    # def test_remove_from_bag(self):
