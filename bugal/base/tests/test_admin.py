from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@londonappdev.com',
            first_name='test_admin',
            last_name='bugal',
            password='password123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            first_name='test_user',
            last_name='bugal',
            email='test@londonappdev.com',
            password='password123'
        )

    def test_users_listed(self):
        """Test that users are listed on the user page"""
        url = reverse('admin:base_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.first_name)
        self.assertContains(res, self.user.email)
