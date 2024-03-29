from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django_resized import ResizedImageField
from django.utils.crypto import get_random_string
from django_cleanup import cleanup


class CustomUserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password=None):

        if not email:
            raise ValueError('Email address must not be empty')

        if not first_name:
            raise ValueError('First name must not be empty')

        if not last_name:
            raise ValueError('Last name must not be empty')
        
        if not password:
            raise  ValueError('Password must not be empty')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, first_name, last_name, password):
        
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


def profile_img_path(self, filename):
    unique_id = get_random_string(length=6)
    return f'profile_images/{self.pk}/{unique_id}.jpg'

@cleanup.ignore
class CustomUser(AbstractBaseUser):

    email           = models.EmailField(verbose_name='Email', max_length=60, unique=True)
    date_joined     = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='Last Login', auto_now=True)
    is_active       = models.BooleanField(default=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    # custom user fields
    first_name      = models.CharField(verbose_name='First Name', max_length=60)
    last_name       = models.CharField(verbose_name='Last Name', max_length=60)
    profile_image   = ResizedImageField(size=[500, 500], crop=['middle', 'center'], upload_to=profile_img_path)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'user'


    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Device(models.Model):
    class DeviceStatus(models.TextChoices):
        ONLINE = 'online', 'online'
        OFFLINE = 'offline', 'offline'

    device_name     = models.CharField(verbose_name='Device Name', max_length=120, unique=True)
    location        = models.CharField(verbose_name='Location', max_length=120)
    install_date    = models.DateField(verbose_name='Install Date')
    install_time    = models.TimeField(verbose_name='Install Time')
    managed_by      = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Managed By")
    created_on      = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.device_name

    class Meta:
        verbose_name = 'device'
        get_latest_by = "created_on"


class Component(models.Model):
    component_name      = models.CharField(verbose_name='Component Name', max_length=120, unique=True)
    device_link         = models.ForeignKey(Device, on_delete=models.CASCADE, verbose_name="Device Link")
    install_date        = models.DateField(verbose_name='Install Date')
    install_time        = models.TimeField(verbose_name='Install Time')
    installed_by        = models.CharField(verbose_name='Installed By', max_length=120)
    created_on          = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device_link}__{self.component_name}"

    class Meta:
        verbose_name = 'component'


def record_img_path(self, filename):
    return f'record_images/{self.record_date}-{self.record_time}.jpg'

class TurbidityRecord(models.Model):

    class VavleControl(models.TextChoices):
        ON = 'on', 'on'
        OFF = 'off', 'off'

    class WaterStatus(models.TextChoices):
        CLEAN = 'clean', 'clean'
        DIRTY = 'dirty', 'dirty'

    record_device       = models.ForeignKey(Device, on_delete=models.CASCADE, verbose_name="Record Device", related_name='records')
    record_date         = models.DateField(verbose_name='Record Date', auto_now_add=True)
    record_time         = models.TimeField(auto_now_add=True, verbose_name='Record Time')
    record_image        = ResizedImageField(size=[300, 300], upload_to=record_img_path, blank=True)
    valve_status        = models.CharField(verbose_name='Vavle Status', max_length=3, choices=VavleControl.choices, blank=True)
    water_status        = models.CharField(verbose_name='Water Status', max_length=5, choices=WaterStatus.choices, blank=True)
    details             = models.CharField(verbose_name='Details', max_length=200)
    created_on          = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.record_device}__{self.record_date}__{self.record_time}__{self.water_status}"

    class Meta:
        verbose_name = 'Turbidity Record'
        ordering = ('created_on',)
        
