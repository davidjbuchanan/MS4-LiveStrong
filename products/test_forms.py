from django.test import TestCase
from .forms import ProductForm

class TestItemForm(TestCase):

    def test_name_is_required(self):
        form = ProductForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_description_is_required(self):
        form = ProductForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0], 'This field is required.')
    
    def test_price_is_required(self):
        form = ProductForm({'price': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0], 'This field is required.')

    def test_all_other_fields_are_not_required(self):
        form = ProductForm({'name': 'name', 'description': 'description description', 'price': '100.00'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ProductForm()
        self.assertEqual(form.Meta.fields, '__all__')
