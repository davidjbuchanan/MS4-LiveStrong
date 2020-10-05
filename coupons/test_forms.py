from django.test import TestCase
from .forms import CouponApplyForm, CouponForm

class TestItemForm(TestCase):

    def test_code_is_required(self):
        form = CouponApplyForm({'code': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('code', form.errors.keys())
        self.assertEqual(form.errors['code'][0], 'This field is required.')

    def test_CouponApplyForm_all_other_fields_are_not_required(self):
        form = CouponApplyForm({'code': 'code1'})
        self.assertTrue(form.is_valid())

    def test_CouponApplyForm_fields_are_explicit_in_form_metaclass(self):
        form = CouponApplyForm()
        self.assertEqual(form.Meta.fields, ('code',))

    def test_CouponForm_code_is_required(self):
        form = CouponForm({'code': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('code', form.errors.keys())
        self.assertEqual(form.errors['code'][0], 'This field is required.')

    def test_valid_from_is_required(self):
        form = CouponForm({'valid_from': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('valid_from', form.errors.keys())
        self.assertEqual(form.errors['valid_from'][0], 'This field is required.')

    def test_valid_to_is_required(self):
        form = CouponForm({'valid_to': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('valid_to', form.errors.keys())
        self.assertEqual(form.errors['valid_to'][0], 'This field is required.')

    def test_discount_is_required(self):
        form = CouponForm({'discount': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('discount', form.errors.keys())
        self.assertEqual(form.errors['discount'][0], 'This field is required.')

    def test_CouponForm_all_other_fields_are_not_required(self):
        form = CouponForm({'code': 'code1', 'valid_from': '2020-10-10 10:10:10', 'valid_to': '2021-10-10 10:10:10', 'discount': '10'})
        self.assertTrue(form.is_valid())

    def test_CouponForm_fields_are_explicit_in_form_metaclass(self):
        form = CouponForm()
        self.assertEqual(form.Meta.fields, '__all__')
