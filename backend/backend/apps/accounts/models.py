from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin




#following codes are written by pugal

class Currencies(models.Model):

    createdAt = models.OneToOneField('common.Countries',on_delete=models.CASCADE)
    updatedAt = models.DateField(auto_now= True)
    country_id = models.FloatField(null=True)
    fraction_unit = models.FloatField(null=True)
    fraction_number = models.IntegerField(default=0)
    iso_code = models.IntegerField(default=0)
    symbol = models.CharField(max_length=24)
    currency = models.CharField(max_length=24)


    def __str__(self):

        return self.currency


class UserRole(models.Model):

    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    user_type = models.CharField(max_length=24, default = None)
    desc = models.CharField(max_length=254)
    permissions = models.CharField(max_length=24)
    html_text = models.CharField(max_length=24)
    createdAt = models.DateField(auto_now= True)

    def __str__(self):

        return self.user_type

'''
class User(models.Model):

    username = models.CharField(max_length=24, default = None)
    email = models.EmailField(null=True, blank=True)
    password = models.CharField(max_length=24, default = None)
    full_name = models.CharField(max_length=24, default = None)
    first_name = models.CharField(max_length=24, default = None)
    last_name = models.CharField(max_length=24, default = None)
    phone_country_code_id = models.IntegerField(default=0)
    is_verified = models.BooleanField(default=False)
    is_verified_phone = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now= True)
    user_role = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    city = models.CharField(max_length=24, default = None)
    state = models.CharField(max_length=24, default = None)
    pincode = models.IntegerField(default=0)
    street = models.CharField(max_length=24, default = None)
    house_no = models.IntegerField(default=0)
    country = models.CharField(max_length=24, default = None)
    district = models.CharField(max_length=24, default = None)
    icc = models.CharField(max_length=24, default = None)
    number = models.IntegerField(default=0)
    company_id = models.IntegerField(default=0)
    website = models.URLField(max_length=200)
    lat = models.ManyToManyField('ponds.Ponds', related_name='latitude')
    lng = models.ManyToManyField('ponds.Ponds', related_name='longitude')
    html_text = models.CharField(max_length=24, default = None)
    updatedAt = models.OneToOneField('common.Countries',on_delete=models.CASCADE)
    last_login_date = models.DateField(auto_now = True)
    signup_date = models.DateField(auto_now = True)
    is_active = models.BooleanField(default = True)
    pending_invite = models.CharField(max_length=24, default = None)
    social_login = models.CharField(max_length=24, default = None)

    #this models has many to many field with Farms dont know the fields


    def __str__(self):

        return self.username

        '''