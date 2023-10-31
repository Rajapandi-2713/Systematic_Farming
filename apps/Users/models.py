from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin,User
from django.contrib.auth.base_user import AbstractBaseUser

# Custom Model Manager
from .managers import UserManager

# Custom User Model
class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=254, unique=True, blank=True)
    first_name = models.CharField( max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    fullname = models.CharField(max_length=100, blank=True)
    profile = models.ImageField(upload_to='profile/', null=True, blank=True)

    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    otp = models.CharField(max_length=6, blank=True, null=True)
    otp_expire = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fullname']
    EMAIL_FIELD = 'email'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        return self.fullname

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.fullname

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)