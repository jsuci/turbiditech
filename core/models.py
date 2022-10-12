from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password=None):

        if not email:
            raise ValueError('Email address must not be empty')

        if not first_name:
            raise ValueError('First name must not be empty')

        if not last_name:
            raise ValueError('Last name must not be empty')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, first_name, last_name, password=None):

        user = self.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser):

    email           = models.EmailField(verbose_name='Email', max_length=60, unique=True)
    date_joined     = models.DateField(verbose_name='Date Joined', auto_now_add=True)
    last_login      = models.DateField(verbose_name='Last Login', auto_now=True)
    is_active       = models.BooleanField(default=True)
    is_admin        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    # is_staff        = models.BooleanField(default=False)

    # custom user fields
    first_name      = models.CharField(verbose_name='First Name', max_length=60)
    last_name       = models.CharField(verbose_name='Last Name', max_length=60)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin