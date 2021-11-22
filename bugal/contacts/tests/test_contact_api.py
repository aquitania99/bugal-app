from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
import uuid

from rest_framework.test import APIClient
from rest_framework import status

# Models
from bugal.base.models import *

# Urls
GET_CONTACTS_URL = reverse('contacts:contact-list')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PrivateClientApiTests(TestCase):
    """Test API Requests that require authentication"""

    def setUp(self):
        self.user = create_user(
            email='test@akela.solutions',
            password='testpass',
            first_name='Test User1',
            last_name='Bugal'
        )

        self.client1 = Contact.objects.create(
            uuid=uuid.uuid4(),
            user=self.user,
            email="client1_test@some.email.com",
            first_name="Test Client 1",
            last_name="Bugal",
            type='client'
        )

        self.client2 = Contact.objects.create(
            uuid=uuid.uuid4(),
            user=self.user,
            email="client2_test@some.email.com",
            first_name="Test Client 2",
            last_name="Bugal",
            type='client'
        )
        
        self.organisation1 = Contact.objects.create(
            uuid=uuid.uuid4(),
            user=self.user,
            org_name="Death Star",
            email="org1_test@some.email.com",
            address_line="306 George St, Sydney, NSW, 2000",
            type='organisation'
        )
        
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_client_success(self):
        """Test create client for logged in user"""
        payload = {'type': 'client', 'first_name': 'Luke', 'last_name': 'Skywalker', 'NDISID': 9000000, 'email': 'lks@tst.org'}
        res = self.client.post(GET_CONTACTS_URL, payload)
        self.assertIsNotNone(res)
        self.assertEquals(res.data['email'], payload['email'])
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_create_organisation_success(self):
        """Test create organisation for logged in user"""
        payload = {'type': 'organisation', 'org_name': 'Empire\'s Death Star', 'NDISID': 5005000, 'email': 'dv@tst.org'}
        res = self.client.post(GET_CONTACTS_URL, payload)
        self.assertIsNotNone(res)
        self.assertEquals(res.data['email'], payload['email'])
        self.assertEquals(res.data['org_name'], payload['org_name'])
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_create_record_without_type(self):
        """Test create client record for logged in user without TYPE"""
        payload = {'org_name': 'Mordor', 'NDISID': 5005000, 'email': 'sauron@tst.org'}
        res = self.client.post(GET_CONTACTS_URL, payload)
        # import pdb; pdb.set_trace()
        self.assertIsNotNone(res)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_clients_success(self):
        """Test retrieving all clients for logged in user"""
        res = self.client.get(GET_CONTACTS_URL)

        self.assertIsNotNone(res)
        self.assertEquals(3, len(res.data['results']))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_retrieve_client_success(self):
        """Test retrieving data for a specific client"""
        get_client_url = reverse('contacts:contact-detail', kwargs={'pk': self.client1.uuid})
        res = self.client.get(get_client_url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['email'], self.client1.email)

    def test_update_client_data(self):
        """Test update specific contact/client data for authenticated user"""
        payload = {'first_name': 'new name', 'last_name': 'new_lastname', 'NDISID': 1000000}
        patch_client_url = reverse('contacts:contact-detail', kwargs={'pk': self.client2.uuid})
        res = self.client.patch(patch_client_url, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        get_client_url = reverse('contacts:contact-detail', kwargs={'pk': self.client2.uuid})
        res2 = self.client.get(get_client_url)

        self.assertEqual(res2.data['first_name'], payload['first_name'])
        self.assertEqual(res2.data['last_name'], payload['last_name'])
        self.assertEqual(res2.data['email'], self.client2.email)

    def test_retrieve_organisation_success(self):
        """Test retrieving data for a specific organisation"""
        get_client_url = reverse('contacts:contact-detail', kwargs={'pk': self.organisation1.uuid})
        res = self.client.get(get_client_url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['email'], self.organisation1.email)
        self.assertEqual(res.data['org_name'], self.organisation1.org_name)

    def test_update_organisation_data(self):
        """Test update specific contact/organisation data for authenticated user"""
        payload = {'org_name': 'Tatooine', 'NDISID': 3000001, 'address_line': "B215 150 Epping Road, Lane Cove, NSW, 2066"}
        patch_client_url = reverse('contacts:contact-detail', kwargs={'pk': self.organisation1.uuid})
        res = self.client.patch(patch_client_url, payload)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        get_client_url = reverse('contacts:contact-detail', kwargs={'pk': self.organisation1.uuid})
        res2 = self.client.get(get_client_url)

        self.assertEqual(res2.data['org_name'], payload['org_name'])
        self.assertEqual(res2.data['NDISID'], payload['NDISID'])
        self.assertEqual(res2.data['email'], self.organisation1.email)
        self.assertNotEqual(res2.data['address_line'], self.organisation1.address_line)
