# Web Technology with Django

A Django-based web development project developed as part of the **Web Technology** course.

The project is being built step-by-step while learning Django, Python, Git, GitHub, MySQL, and web application development.

---

## 📚 Course Resources

Official course resources:

https://ritushishir.github.io/web-technology-with-django/

The website contains:

* Course slides
* Unit-wise notes
* Detailed topic explanations
* Class resources
* Web Technology with Django materials

---

## 🛠️ Technologies Used

* **Python 3.10+**
* **Django**
* **MySQL**
* **Git**
* **GitHub**
* **HTML/CSS**
* **JavaScript** *(to be covered)*

---

## 📋 Initial Requirements

Before starting the project, the following were installed/configured:

* Python 3.10 or newer
* Git
* MySQL
* GitHub account
* VS Code / suitable code editor
* Python virtual environment

---

# 🚀 Project Setup

## 1. Create the Project Directory

```powershell
mkdir web-technology-with-django
cd web-technology-with-django
```

---

## 2. Initialize Git

```powershell
git init
git branch -M main
```

This initializes the project as a Git repository and sets the default branch to `main`.

---

## 3. Create Python Virtual Environment

```powershell
python -m venv .venv
```

The virtual environment keeps the project's Python dependencies isolated from the system Python installation.

---

## 4. Activate Virtual Environment

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell execution policy causes an issue:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, the terminal should show:

```text
(.venv) PS C:\web-technology-with-django>
```

---

## 5. Check Python Version

```powershell
python --version
```

The project requires:

```text
Python 3.10 or newer
```

---

## 6. Upgrade pip

```powershell
python -m pip install --upgrade pip
```

---

## 7. Install Django

```powershell
python -m pip install django
```

Check the Django version:

```powershell
django-admin --version
```

---

# 🏗️ Create Django Project

Create the Django project using:

```powershell
django-admin startproject config .
```

The `.` means that Django should create the project in the current directory.

The project structure becomes approximately:

```text
web-technology-with-django/
│
├── .venv/
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
│
└── .gitignore
```

---

# ▶️ Run Django Development Server

Start the development server:

```powershell
python manage.py runserver
```

The development server normally runs at:

```text
http://127.0.0.1:8000/
```

Open the address in a browser to verify that Django is working.

---

# 🎵 Create Songs Application

The first Django application created in this project is `songs`.

Create it with:

```powershell
python manage.py startapp songs
```

The application structure is:

```text
songs/
│
├── migrations/
│   └── __init__.py
│
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

---

# ⚙️ Register the Songs App

Add the `songs` application to:

```text
config/settings.py
```

Inside `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # Django default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Project apps
    'songs',
]
```

---

# 🔗 Songs URL Configuration

A separate URL configuration was created for the `songs` application.

File:

```text
songs/urls.py
```

Current configuration:

```python
from django.urls import path
from songs import views

urlpatterns = [
    path('', views.song_list, name='song_list'),
    # path('<int:song_id>/', views.song_detail, name='song_detail'),
]
```

The commented route was intended for individual song details:

```text
/songs/1/
/songs/2/
/songs/3/
```

---

# 🌐 Project URL Configuration

The main URL configuration is located at:

```text
config/urls.py
```

The `songs` URLs are connected to the main project using:

```python
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('songs/', include('songs.urls')),
]
```

Therefore:

```text
/songs/
```

will be handled by the `songs` application.

---

# 👁️ Songs Views

The application's views are located in:

```text
songs/views.py
```

The current project uses:

```python
from django.http import HttpResponse


def song_list(request):
    return HttpResponse("Song List")
```

The view can be accessed through:

```text
http://127.0.0.1:8000/songs/
```

---

# 🗄️ MySQL

MySQL was also prepared as part of the course environment.

The MySQL shell can be checked using:

```powershell
mysql --version
```

Login:

```powershell
mysql -u root -p
```

The Django project can later be configured to use MySQL through `config/settings.py`.

---

# 🧪 Django Database Migration

Django's initial database migrations can be applied using:

```powershell
python manage.py migrate
```

To create migrations after modifying models:

```powershell
python manage.py makemigrations
```

Then:

```powershell
python manage.py migrate
```

---

# 📦 Python Dependencies

Project dependencies are stored in:

```text
requirements.txt
```

Generate the file using:

```powershell
python -m pip freeze > requirements.txt
```

To install dependencies on another machine:

```powershell
python -m pip install -r requirements.txt
```

> **Note:** `.venv` should not be uploaded to GitHub. Only `requirements.txt` should be committed.

---

# 🔐 .gitignore

The virtual environment and Python-generated files should be excluded from Git.

Example `.gitignore`:

```gitignore
# Virtual environment
.venv/

# Python cache
__pycache__/
*.py[cod]

# Django
db.sqlite3

# Environment variables
.env

# IDE
.vscode/
.idea/
```

---

# 📌 Git Workflow

Check the current status:

```powershell
git status
```

Add files:

```powershell
git add .
```

Create a commit:

```powershell
git commit -m "Add songs app"
```

Push to GitHub:

```powershell
git push origin main
```

Check the commit history:

```powershell
git log --oneline
```

---

# 🔄 Typical Development Workflow

For future development, use:

```powershell
# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Start Django server
python manage.py runserver
```

After making changes:

```powershell
git status
git add .
git commit -m "Describe the changes"
git push origin main
```

---

# 📁 Current Project Structure

The project currently looks approximately like this:

```text
web-technology-with-django/
│
├── .venv/
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── songs/
│   ├── migrations/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ✅ Completed So Far

* [x] Installed Python 3.10+
* [x] Installed Git
* [x] Set up MySQL
* [x] Created GitHub repository
* [x] Created project directory
* [x] Initialized Git repository
* [x] Created `main` branch
* [x] Created Python virtual environment
* [x] Activated virtual environment
* [x] Upgraded pip
* [x] Installed Django
* [x] Created Django project
* [x] Started Django development server
* [x] Created `songs` Django application
* [x] Configured `songs` application
* [x] Created `songs/urls.py`
* [x] Connected `songs` URLs with the main project
* [x] Created `song_list` view
* [x] Tested Django routing
* [x] Used Git commits
* [x] Pushed project to GitHub
* [x] Created `requirements.txt`

---

# 🔜 Next Steps

The next development tasks are:

1. Create the `Song` model
2. Configure the database
3. Run migrations
4. Register the model in Django Admin
5. Create sample song data
6. Display songs dynamically
7. Create song detail pages
8. Add HTML templates
9. Add CSS styling
10. Continue building the complete Django application

---

## 👨‍💻 Project

**Project:** Web Technology with Django

**Framework:** Django

**Language:** Python

**Database:** MySQL

**Version Control:** Git + GitHub

**Primary Application:** `songs`
