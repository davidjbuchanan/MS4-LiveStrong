from django.test import TestCase
from .forms import CommentForm, UserBlogForm, EditPost

class TestCommentForm(TestCase):

    def test_comment_name_is_required(self):
        form = CommentForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_comment_email_is_required(self):
        form = CommentForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_comment_body_is_required(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_comment_all_other_fields_are_not_required(self):
        form = CommentForm({'body': 'body1', 'name': 'name1', 'email': 'email@email.com'})
        self.assertTrue(form.is_valid())

    def test_comment_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('name', 'email', 'body'))

class TestUserBlogForm(TestCase):

    def test_add_post_title_is_required(self):
        form = UserBlogForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_add_post_body_is_required(self):
        form = UserBlogForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_add_post_slug_is_required(self):
        form = UserBlogForm({'slug': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('slug', form.errors.keys())
        self.assertEqual(form.errors['slug'][0], 'This field is required.')

    def test_add_post_all_other_fields_are_not_required(self):
        form = UserBlogForm({'title': 'title1', 'body': 'body1', 'slug': 'slug1'})
        self.assertTrue(form.is_valid())

    def test_add_post_excludes_are_explicit_in_form_metaclass(self):
        form = UserBlogForm()
        self.assertEqual(form.Meta.exclude, ('publish', 'created', 'updated', 'status', 'author'))

class TestEditPost(TestCase):

    def test_publish_status_is_required(self):
        form = EditPost({'status': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('status', form.errors.keys())
        self.assertEqual(form.errors['status'][0], 'This field is required.')

    def test_publish_status_all_other_fields_are_not_required(self):
        form = EditPost({'status': 'draft'})
        self.assertTrue(form.is_valid())

    def test_publish_status_excludes_are_explicit_in_form_metaclass(self):
        form = EditPost()
        self.assertEqual(form.Meta.exclude, ('publish', 'created', 'updated', 'author', 'title', 'body', 'slug'))
