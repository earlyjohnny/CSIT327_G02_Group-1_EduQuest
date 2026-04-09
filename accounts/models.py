from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


class Profile(models.Model):
    student_num = models.CharField(max_length=50, primary_key=True, unique=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile"
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    year_level = models.CharField(max_length=10)

    class Meta:
        db_table = "profile"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_num})"


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)

    org = models.ForeignKey("organizations.Organization", on_delete=models.CASCADE, related_name="roles", null=True,
        blank=True)
    role_title = models.CharField(max_length=100)
    access_level = models.IntegerField(default=1)
    is_officer = models.BooleanField(default=False)

    class Meta:
        db_table = "role"

    def __str__(self):
        return f"{self.role_title} - {self.org}"


class Membership(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("pending", "Pending"),
    ]

    membership_id = models.AutoField(primary_key=True)
    student_num = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        to_field="student_num",
        related_name="memberships",
    )

    org = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="memberships",
        null=True,
        blank=True
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="memberships",
    )
    join_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "membership"
        # A student cannot have more than one active membership per organization

        unique_together = [("student_num", "org")]

    def __str__(self):
        return f"{self.student_num} - {self.org} ({self.status})"