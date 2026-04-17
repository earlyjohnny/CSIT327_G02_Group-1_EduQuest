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
