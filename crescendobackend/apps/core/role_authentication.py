from typing import Optional
from django.contrib.auth.backends import BaseBackend
from django.http import HttpRequest
from .models.role import Role


class RoleBackend(BaseBackend):
    def authenticate(self,
                     request: Optional[HttpRequest] = None,
                     role: Optional[str] = None,
                     token: Optional[str] = None) -> Optional[Role]:
        # TODO: implement for real
        if role is None:
            return None
        return self.get_user(role)

    def get_user(self, user_id: str) -> Optional[Role]:
        try:
            return Role.objects.get(name=user_id)
        except Role.DoesNotExist:
            return None
