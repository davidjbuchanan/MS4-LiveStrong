from django.test import TestCase
from .forms import UserProfileForm

class TestUserProfileForm(TestCase):

    def test_all_other_fields_are_not_required(self):
        form = UserProfileForm({})
        self.assertTrue(form.is_valid())

    def test_excludes_are_explicit_in_form_metaclass(self):
        form = UserProfileForm()
        self.assertEqual(form.Meta.exclude, ('user',))
