from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, password):
        if not email:
            raise ValueError("Users must have an Email Address.")
        if not password:
            raise ValueError("Password is not provided.")
        email = self.normalize_email(email)
        user = self.model(
            email=email,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password,):
        user = self.create_user(
            email=email,
            password=password,)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=255, unique=True, verbose_name='username')

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = UserManager()

    @property
    def is_staff(self):
        "is the user a member od staff?"
        return self.is_superuser

    class Meta:
        verbose_name = "User"
        verbose_name_plural = 'Users'
