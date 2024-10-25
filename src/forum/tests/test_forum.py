from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import Client, TestCase

from forum.utils.samples import sample_comment, sample_post


class TestPost(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = get_user_model()(username="Oleg")
        self.user.set_password("12345678")
        self.user.save()

    def test_max_length_post_title(self):
        with self.assertRaises(ValidationError):
            sample_post(self.user, title="S" * 500)


class TestComment(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = get_user_model()(username="Oleg")
        self.user.set_password("12345678")
        self.user.save()

        self.post = sample_post(self.user, title="S" * 100)

    def test_create_comment(self):
        sample_comment(self.user, conversation=self.post, content="test comment")
