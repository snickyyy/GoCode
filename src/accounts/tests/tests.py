from http import HTTPStatus

from django.contrib.auth import get_user_model, login
from django.test import Client, TestCase
from django.urls import reverse_lazy


class TestAuth(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = get_user_model()(username="Oleg")
        self.user.set_password("12345678")
        self.user.save()

        self.manager = get_user_model()(email="manager@example.com", is_staff=True)
        self.manager.set_password("12345678")
        self.manager.save()

    def test_user_login_wrong_username(self):
        user_login = self.client.login(username="Oleg1", password="12345678")
        self.assertFalse(user_login)

    def test_user_login_wrong_password(self):
        user_login = self.client.login(username="Oleg", password="123456789wrong")
        self.assertFalse(user_login)

    def test_user_login_correct(self):
        user_login = self.client.login(username="Oleg", password="12345678")
        self.assertTrue(user_login)

    def test_admin_panel_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy("admin:index"))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_admin_panel_manager(self):
        self.client.force_login(self.manager)
        response = self.client.get(reverse_lazy("admin:index"))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_user_access_index_page(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy("index"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
