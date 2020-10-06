from django.test import TestCase
from blog.models import Post


class TestView(TestCase):

    def test_post_list(self):  # ok
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/list.html')

    def test_post_detail(self): # errors
        item.publish = Post.objects.create(publish='2020-10-10', slug='slug1')
        response = self.client.get(f'/blog/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/detail.html')

    def test_draft_list(self):  # needs superuser
        response = self.client.get('/blog/drafts/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/drafts.html')
