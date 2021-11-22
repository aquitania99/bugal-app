from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

# Models
from bugal.base.models import User, RateModel

TEST_UUIDS = '9a221efa-6cb9-4857-9f1e-57cfc16078a6'
TEST_RATE_PK = 1
CREATE_USER_URL = reverse('users:user-signup')
GET_USER_RATES_URL = reverse('users:rate-list')
GET_USER_RATE_URL = reverse('users:rate-detail', kwargs={'pk': TEST_RATE_PK})
LOGIN_USER_URL = reverse('users:user-login')

def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(APITestCase):
    """Test the users API (public)"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test creating user with valid payload is successful"""
        payload = {
            'email': 'test@akela.solutions',
            'password': 'Pass@word01'
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_user_exists(self):
        """Test creating a user that already exists fails"""
        payload = {
            'email': 'test@akela.solutions',
            'password': 'Pass@word01'
        }
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test that the password must be more than 5 characters"""
        payload = {
            'email': 'test@akela.solutions',
            'password': 'Pass'
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)

    def test_login_user_invalid_credentials(self):
        """Token is not created if invalid credentials are given"""
        create_user(email='test@akela.solutions', password='testpass')
        payload = {'email': 'test@akela.solutions', 'password': 'wrong'}
        res = self.client.post(LOGIN_USER_URL, payload)

        self.assertNotIn('access_token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_non_existent_user(self):
        """Test that token is not created if user doesn't exist"""
        payload = {'email': 'test@akela.solutions', 'password': 'testpass'}
        res = self.client.post(LOGIN_USER_URL, payload)
        self.assertNotIn('access_token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_user_missing_field(self):
        """Test that email and password are required"""
        res = self.client.post(LOGIN_USER_URL, {'email': 'one', 'password': ''})
        self.assertNotIn('access_token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_user_unauthorized(self):
        """Test that authentication is requiered for users"""
        res = self.client.get(GET_USER_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateUserApiTests(APITestCase):
    """Test API Requests that require authentication"""

    def setUp(self):
        self.user = create_user(
            uuid=TEST_UUIDS,
            email='test@akela.solutions',
            password='testpass',
            first_name='BugalUser',
            last_name='Test',
            is_verified=True
        )
        
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_login_user_valid_credentials(self):
        """Test that a token is created for the user"""
        payload = {'email': 'test@akela.solutions', 'password': 'testpass'}
        res = self.client.post(LOGIN_USER_URL, payload)
        self.assertIn('access_token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrieve_profile_success(self):
        """Test retrieving profile for logged in user"""
        res = self.client.get(GET_USER_URL)
        # pdb.set_trace()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['user']['email'], 'test@akela.solutions')
        self.assertTrue(res.data['user']['is_verified'])

    def test_post_me_not_allowed(self):
        """Test that POST is not allowed on the me url"""
        res = self.client.post(GET_USER_URL, {})

        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    # Create User Business (ABN)
    def test_create_user_business(self):
        """Test add ABN to the user profile"""
        
        payload = {
            "abn": 10000000001,
            "is_taxable": True,
            "payment_terms":  1
        }
        
        res = self.client.patch(GET_USER_URL, payload)
        self.user.refresh_from_db()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue(res.data, True)
    
    # Create Bank Account
    def test_create_user_bank_account(self):
        """Test add Bank Account to the user profile"""
        
        payload = {
            "bank_bsb": "908789",
            "bank_account": "22214445",
            "bank_name": "NAB"
        }
        
        res = self.client.patch(GET_USER_URL, payload)
        self.user.refresh_from_db()
        # import pdb; pdb.set_trace()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue(res.data, True)

    # Update User & User Profile
    def test_update_user_profile(self):
        from datetime import date
        """Test updating the user profile for authenticated user"""
        payload = {'first_name': 'new name', 'dob': '1975-01-25'}
        res = self.client.patch(GET_USER_URL, payload)
        
        self.user.refresh_from_db()
        # pdb.set_trace()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue(res.data, True)
        self.assertEqual(self.user.first_name, payload['first_name'])
        self.assertEqual(date(1975,1,25), self.user.dob)

    def test_update_user_abn(self):
        """Test updating the user profile with ABN"""
        payload = {
            "abn": 333355555890,
            "is_taxable": True,
            "payment_terms": 15
        }
        
        res = self.client.patch(GET_USER_URL, payload)
        self.user.refresh_from_db()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue(res.data, True)
    
    def test_update_user_bank_account(self):
        """Test updating the user profile with Bank Account"""
        payload = {
            "bank_bsb": "908789",
            "bank_account": "22214445",
            "bank_id": 1
        }
        
        res = self.client.patch(GET_USER_URL, payload)
        self.user.refresh_from_db()
        # import pdb; pdb.set_trace()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue(res.data, True)
