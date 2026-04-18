# EduQuest

A centralized digital management platform for campus organizations, streamlining event registration, membership tracking, and resource allocation.

---

## Group Members

| Name     | Assigned App | Scope |
|----------|-------------|-------|
| Guimoc   | `accounts` | User & profile management |
| Custodio | `organizations` | Organizations, roles, and categories |
| Eupeña   | `events` | Events, venues, and logistics |
| Guimoc   | `registrations` | Registrations and attendance tracking |
| Sultan   | `finances` | Budget requests and equipment |
| Español  | `communications` | Announcements, feedback, and documents |

---

## Project Structure

```
EduQuest/
├── EduQuest/                  # Project configuration
│   ├── settings.py            # Django settings
│   ├── urls.py                # Root URL configuration
├── accounts/                  # User, Profile, Role, Membership
├── organizations/             # Organization, Category
├── events/                    # Event, Venue
├── registrations/             # Registration, Attendance
├── finances/                  # BudgetRequest, Equipment, EventEquipment
├── communications/            # Announcement, Feedback, Document
├── manage.py
└── README.md
```

---

## Requirements

- Python 3.13+
- Django 6.0+

---

## How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/earlyjohnny/CSIT327_G02_Group-1_EduQuest.git
cd EduQuest
```

### 2. Create and activate a virtual environment
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install django
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Create a superuser
```bash
python manage.py shell
```
```python
from accounts.models import User
User.objects.create_superuser(email='admin@admin.com', password='yourpassword')
exit()
```

### 6. Run the development server
```bash
python manage.py runserver 8080
```

### 7. Open in browser
```
http://127.0.0.1:8080
```

You will be redirected to the login page automatically.

---

## URL Structure

| URL | Description |
|-----|-------------|
| `/` | Index — redirects to login |
| `/accounts/login/` | Login page |
| `/accounts/logout/` | Logout |
| `/accounts/index/` | Home page with app navigation |
| `/organizations/` | Organizations app |
| `/events/` | Events app |
| `/registrations/` | Registrations app |
| `/finances/` | Finances app |
| `/communications/` | Communications app |
| `/admin/` | Django admin panel (superusers only) |

---

## Notes

- Superusers are redirected to `/admin/` after login
- Regular users are redirected to `/accounts/index/` after login
- Passwords are hashed using Django's built-in `set_password()` — never stored as plain text
- The custom `User` model uses email instead of username for authentication
