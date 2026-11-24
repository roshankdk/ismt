from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Category, Post


class BlogPublicTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user('roshan', password='pass12345')
        cls.cat = Category.objects.create(name='Travel')
        cls.post = Post.objects.create(title='Trek to Poon Hill', author=cls.user, category=cls.cat, content='Great views.')
        cls.draft = Post.objects.create(title='Secret Draft', author=cls.user, content='Hidden.', published=False)

    def test_slug_is_generated_and_unique(self):
        self.assertEqual(self.post.slug, 'trek-to-poon-hill')
        dup = Post.objects.create(title='Trek to Poon Hill', author=self.user, content='Again')
        self.assertEqual(dup.slug, 'trek-to-poon-hill-2')

    def test_list_is_public_and_hides_drafts(self):
        r = self.client.get(reverse('blog_list'))
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Trek to Poon Hill')
        self.assertNotContains(r, 'Secret Draft')

    def test_detail_is_public(self):
        r = self.client.get(self.post.get_absolute_url())
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, 'Great views.')

    def test_unknown_slug_and_draft_return_404(self):
        self.assertEqual(self.client.get('/blog/post/nope/').status_code, 404)
        self.assertEqual(self.client.get(self.draft.get_absolute_url()).status_code, 404)

    def test_category_slug_is_generated(self):
        self.assertEqual(self.cat.slug, 'travel')
