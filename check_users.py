import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EduQuest.settings')
django.setup()

from accounts.models import User, Profile

# Create a test user with a known password (or reset if exists)
email = 'testfinances@test.com'
password = 'finances123'

user, created = User.objects.get_or_create(email=email)
user.set_password(password)
user.save()

# Create a profile for this user
profile, p_created = Profile.objects.get_or_create(
    user=user,
    defaults={
        'student_num': '20210001',
        'first_name': 'April John',
        'last_name': 'Guimoc',
        'course': 'BSIT',
        'year_level': '3rd Year',
    }
)

if created:
    print(f"Created new user: {email}")
else:
    print(f"User already existed, password reset: {email}")

if p_created:
    print(f"Created profile: {profile}")
else:
    print(f"Profile already existed: {profile}")

print(f"\n--- Login credentials ---")
print(f"Email:    {email}")
print(f"Password: {password}")
