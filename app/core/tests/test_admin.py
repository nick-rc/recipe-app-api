from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminSiteTests(TestCase, Client):

    def setup(self):
        """Create test client, user, make sure logged in, create regular user"""
        self.client = Client()
        self.admin = get_user_model.objects.create_superuser(
            email='admin@test.com',
            password='password'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model.objects.create_user(
            email = 'user@test.com',
            password = 'password',
            name = 'Test User Full Name'
        )

    def test_users_listed(self):
        """Test that users are correctly listed"""
        url = reverse('admin:core_user_changelist')
        res = self.Client.get(url)

        self.AssertContains(res, self.user.name)
        self.AssertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

# ENDFILE
