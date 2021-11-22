from django.test import TestCase

from bugal.base.models import Bank, Contact, User
from bugal.base.serializers import BankModelSerializer


class BankModelTest(TestCase):
    """Test Bank model"""
    
    def setUp(self):
        self.bank0 = Bank.objects.create(
            name="NAB",
            description="National Australian Bank"
        )
    
    def test_add_new_bank(self):
        """add new bank"""
        bank1 = Bank.objects.create(
            name="CBA",
            description="Commonwealth Bank of Australia"
        )
        
        self.assertEqual(bank1.name, "CBA")
    
    def test_add_new_client_contact(self):
        """add a new client to Contact Model"""
        

class ContactModelTest(TestCase):
    """Test Contact model"""
    def setUp(self) -> None:
        self.user = User.objects.create(
            email="test_user@bugal.com.au",
            first_name="test_user",
            last_name="bugal"
        )

    def test_contact_client(self):
        """Test adding a new contact of type Client."""
        client = Contact.objects.create(
            user=self.user,
            type='Cli',
            first_name="Test Name",
            last_name="Test Lastname",
            email="client_test@test.org",
            address_line="u2 21-25 High St., Caringbah, NSW 2229"
        )

        self.assertEqual(client.email, "client_test@test.org")

    def test_contact_organisation(self):
        """Test adding a new contact of type Client."""
        organisation = Contact.objects.create(
            user=self.user,
            type='Org',
            org_name="Test Organisation Nname",
            email="organisation_test@test.org",
            address_line="u2 21-25 High St., Caringbah, NSW 2229"
        )

        self.assertNotEqual(organisation.email, "client_test@test.org")
        self.assertEqual(organisation.type, "Org")

    def test_get_all_contacts(self):
        client = Contact.objects.create(
            user=self.user,
            type='Cli',
            first_name="Test Name",
            last_name="Test Lastname",
            email="client_test@test.org",
            address_line="u2 21-25 High St., Caringbah, NSW 2229"
        )

        organisation = Contact.objects.create(
            user=self.user,
            type='Org',
            org_name="Test Organisation Name",
            email="organisation_test@test.org",
            address_line="u2 21-25 High St., Caringbah, NSW 2229"
        )

        clients = Contact.objects.all()

        self.assertIsNotNone(clients)
        self.assertEquals(clients.count(), len(clients))
        self.assertEquals(clients.get(type='Org').org_name, organisation.org_name)
        self.assertEquals(clients.get(type='Cli').first_name, client.first_name)
