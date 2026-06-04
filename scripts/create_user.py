from django.contrib.auth import get_user_model
User = get_user_model()
email = 'sultan@example.com'
pwd = 'SultanPass123!'
created = False
if not User.objects.filter(email=email).exists():
    User.objects.create_superuser(email, pwd)
    created = True
print('CREATED' if created else 'EXISTS')
u = User.objects.get(email=email)
print('email:', u.email, 'is_superuser:', u.is_superuser)
