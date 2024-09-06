from django.test import TestCase
from .models import  Post ,Author
from django.utils import timezone

# Create your tests here.
class PostModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='Bretech', email='bryotechs@gmail.com')
    def test_post_str(self):
        post = Post (
            title='My First Post',
            content='This is my first blog post.',
            status='Complete',  # or 'Draft'
            created_at=timezone.now().date(), 
            author= self.author,
        )
        expected_str ="{self.title} {self.content} {self.status} {self.author},{self.created_at}"
        
        self.assertEqual(str(post), expected_str)