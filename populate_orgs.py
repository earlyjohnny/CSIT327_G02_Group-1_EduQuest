import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EduQuest.settings')
django.setup()

from organizations.models import Category, Organization

# Create a category
cat, _ = Category.objects.get_or_create(
    category_name="Student Council",
    defaults={"description": "Main student body council"}
)

# Create an organization
org, _ = Organization.objects.get_or_create(
    org_name="Computer Science Society",
    acronym="CSS",
    cat=cat,
    defaults={"description": "Organization for CS students"}
)

print(f"Created category: {cat.category_name}")
print(f"Created organization: {org.org_name}")
