from django.test import TestCase


class TestView(TestCase):

    def test_post_list(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/list.html')

    def test_draft_list(self):
        response = self.client.get('/blog/drafts/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/drafts.html')
