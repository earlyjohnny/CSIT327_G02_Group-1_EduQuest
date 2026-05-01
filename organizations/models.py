from django.db import models


class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name


class Organization(models.Model):
    org_id = models.AutoField(primary_key=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    org_name = models.CharField(max_length=100, null=False)
    acronym = models.CharField(max_length=20, null=False)
    description = models.TextField(null=True, blank=True)
    date_founded = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'organization'

    def __str__(self):
        return self.org_name


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    type = models.IntegerField(default=1)  # 1 = student, 0 = teacher

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username
