from django.test import TestCase
from django.contrib.auth import get_user_model

from django.urls import reverse
from .models import Post
class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
        username='testuser',
        email='test@email.com',
        password='secret'
        )
        self.post = Post.objects.create(
        titulo='A good title',
        descripcion='Nice body content',
        cuerpo= 'Este es el cuerpo',
        autor=self.user,
        )
    def test_string_representation(self):
        post = Post(titulo='A sample title')
        self.assertEqual(str(post), post.titulo)
    def test_post_content(self):
        self.assertEqual(f'{self.post.titulo}', 'A good title')
        self.assertEqual(f'{self.post.autor}', 'testuser')
        self.assertEqual(f'{self.post.descripcion}', 'Nice body content')
        self.assertEqual(f'{self.post.cuerpo}', 'Este es el cuerpo')
    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
