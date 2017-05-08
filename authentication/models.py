
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import Group, PermissionsMixin
from django.core.mail import send_mail
from django.db import models

# Create your models here.


class AccountManager(BaseUserManager):
            
    def create_user(self, email, password=None, **kwargs):
        # Ensure that an email address is set
        if not email:
            raise ValueError('Users must have a valid e-mail address')

        account = self.model(
            email=self.normalize_email(email),
            first_name=kwargs.get('first_name', None),
            last_name=kwargs.get('last_name', None)
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password=None, **kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_superuser = True
        account.is_staff = True
        account.save()
        return account
    
    
class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, null=True)
    
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    is_staff = models.BooleanField(default=False, blank=True,
                                   help_text='Designates whether this user should be treated as'
                                             'active. Unselect this instead of deleting accounts.')
    is_active = models.BooleanField(default=True)
    objects = AccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_absolute_url(self):
        return "/users/{0}/".format(self.email)

    def get_full_name(self):
        full_name = "{0} {1}".format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])
        

        
        

