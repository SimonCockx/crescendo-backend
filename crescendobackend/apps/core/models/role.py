from typing import List, Tuple
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class RoleManager(models.Manager):
    pass


class Role(PermissionsMixin, models.Model):
    name = models.CharField(max_length=255, unique=True)

    objects = RoleManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS: List[str] = []

    def __str__(self) -> str:
        return self.name

    def natural_key(self) -> Tuple[str]:
        return self.name,

    @property
    def is_anonymous(self) -> bool:
        """
        Always returns False. This is a way of comparing User objects to
        anonymous users.
        """
        return False

    @property
    def is_authenticated(self) -> bool:
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

