from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def _create_user(self, email, is_staff, is_superuser, role, **extra_fields):

        if not email:
            raise ValueError('unique email must be required')

        password = extra_fields.pop('password', None)

        user = self.model(
            email=email,
            is_admin=is_staff,
            is_superuser=is_superuser,
            role=role,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, **extra_fields):
        from apps.user.models import RoleChoice
        return self._create_user(email, False, False, RoleChoice.USER, **extra_fields)

    def create_superuser(self, email, **extra_fields):
        from apps.user.models import RoleChoice
        return self._create_user(email, True, True, RoleChoice.ADMIN, **extra_fields)
