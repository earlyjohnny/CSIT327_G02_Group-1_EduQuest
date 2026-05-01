import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EduQuest.settings')
django.setup()

from django.contrib.auth.models import User

# Check if admin already exists
if not User.objects.filter(username='admin').exists():
    # If using email login or if they want username to be 'admin@gmail.com' or just 'admin'
    User.objects.create_superuser('admin', 'admin@gmail.com', 'admin')
    print("Superuser created: username 'admin', email 'admin@gmail.com', password 'admin'")
else:
    u = User.objects.get(username='admin')
    u.set_password('admin')
    u.email = 'admin@gmail.com'
    u.save()
    print("Superuser 'admin' password and email updated.")

if not User.objects.filter(username='admin@gmail.com').exists():
    User.objects.create_superuser('admin@gmail.com', 'admin@gmail.com', 'admin')
    print("Superuser created: username 'admin@gmail.com', email 'admin@gmail.com', password 'admin'")
