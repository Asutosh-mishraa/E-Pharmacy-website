from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class MyUserManager(BaseUserManager):
    def create_user(self, name, mobile, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            name=name,
            mobile=mobile,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,  name, mobile, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            name=name,
            mobile=mobile,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    name = models.CharField(max_length=255, default=None)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    mobile = models.CharField(max_length=10, default=None)
    #address = models.TextField(default=None)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'mobile']

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

class Address(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.DO_NOTHING)
    addr_line1 = models.TextField(default=None)
    addr_line2 = models.TextField(default=None)
    pin = models.CharField(max_length=10,default=None)
    city = models.CharField(max_length=50,default=None)
    state = models.CharField(max_length=20,default=None)
    country = models.CharField(max_length=20,default="India")
    phone_number = models.CharField(max_length=20,default=None) 
    alt_email = models.TextField(default="abc@gmail.com")

    

    def __str__(self):
        return self.addr_line1+" "+self.addr_line2+" "+self.city