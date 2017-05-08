from django.test import TestCase

# Create your tests here.
from authentication.models import AccountManager, Account


class AccountModelTest(TestCase):
    def test_except_email(self):
        first_item = Account.objects.create_user(
            email='test2@example.com',
            password='123456789',
        )
        second_item = Account.objects.create_superuser(
            email='test@example.com',
            password='123456789',
            username='test',
            firstName='fist test',
            lastName='last test',
        )
        third_item = Account.objects.create_superuser(
            email='test1@example.com',
            password='123456789',
            username='test1',
            firstName='first test1',
            lastName='last test1'
        )

        self.assertEqual(Account.objects.all().count(), 3)
        self.assertEqual(Account.objects.filter(is_superuser=True).count(), 2)

