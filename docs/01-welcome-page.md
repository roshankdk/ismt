# Your First Django Page: "Welcome to Django World"

In this lesson we make a web page that shows this heading:

> # Welcome to Django World

---

## What We Will Learn

How a request travels in Django:

```
Browser  →  Project urls.py  →  App urls.py  →  View  →  Template (HTML)
```

| Part             | What it does                                       |
|------------------|----------------------------------------------------|
| Project urls.py  | The main reception desk. Sends a request to the right app. |
| App urls.py      | The app's own desk. Picks which view will run.     |
| View             | A Python function that sends back the page.        |
| Template         | The HTML file the browser shows.                   |

---

## Before You Start

You should already have:

- A Django project called `weblinks_site`
- A virtual environment called `venv`

Open a terminal in the project folder (the one with `manage.py`) and turn on the virtual environment:

```bash
source venv/bin/activate
```

> On Windows use: `venv\Scripts\activate`

---

## Step 1: Create an App

A Django **project** is the whole website. An **app** is one part of it.
Let's make an app called `home`:

```bash
python manage.py startapp home
```

Now you will see a new `home` folder with files like `views.py`, `models.py` and `apps.py`.

---

## Step 2: Register the App

Django must know about our new app.
Open `weblinks_site/settings.py` and add `'home'` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',          # our new app
]
```

---

## Step 3: Create the HTML Template

Inside the `home` folder, make a new folder called `templates`.
Inside `templates`, make a file called `index.html`:

```
home/
└── templates/
    └── index.html
```

Write this in `home/templates/index.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My First Django Page</title>
</head>
<body>
    <h1>Welcome to Django World</h1>
</body>
</html>
```

> Django looks inside each app's `templates` folder on its own,
> because `APP_DIRS` is set to `True` in `settings.py`.

---

## Step 4: Write a View

A **view** is a Python function. It gets a request and sends back a page.

Open `home/views.py` and write:

```python
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
```

- `request`: the message from the browser
- `render()`: takes our HTML file and sends it back to the browser

---

## Step 5: Create the App's urls.py

The `home` app does not come with a `urls.py` file, so we make one.

Create a new file `home/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.index),
]
```

- `'hello/'`: the page address, so our page opens at `/hello/`
- `views.index`: the view function to run
- `from . import views`: the `.` means "from this same folder"

---

## Step 6: Connect the App to the Project

Now tell the project to send requests to the `home` app.

Open `weblinks_site/urls.py` and change it to:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]
```

- `include('home.urls')` means: "let the home app handle these URLs"

---

## Step 7: Run the Server

```bash
python manage.py runserver
```

Open this address in your browser:

```
http://127.0.0.1:8000/hello/
```

You should see:

> # Welcome to Django World

To stop the server, press `Ctrl + C`.

---

## Final Folder Structure

```
ismt_django/
├── manage.py
├── weblinks_site/
│   ├── settings.py      ← added 'home'
│   └── urls.py          ← added include('home.urls')
└── home/
    ├── views.py         ← index view
    ├── urls.py          ← new file
    └── templates/
        └── index.html   ← our HTML page
```

---

## Common Mistakes

| Error you see                         | What to check                                              |
|---------------------------------------|------------------------------------------------------------|
| `TemplateDoesNotExist: index.html`    | Is the file in `home/templates/`? Is `'home'` in `INSTALLED_APPS`? |
| `ModuleNotFoundError: No module named 'home'` | Is the `home` folder next to `manage.py`?          |
| `NameError: name 'include' is not defined` | Did you write `from django.urls import path, include`? |
| `python: command not found` or `No module named django` | Did you turn on the virtual environment? |
| Page did not change                   | Save all files, then refresh the browser.                  |

---

## Practice Tasks

1. Change the heading to your own name, for example `Welcome, Ram!`
2. Add a `<p>` paragraph under the heading about yourself.
3. **Challenge:** Make an `about` page at `http://127.0.0.1:8000/about/`.
   - Hint: make `about.html`, add an `about` view, and add `path('about/', views.about)` in `home/urls.py`.

---

**Next:** [Lesson 2: How the Welcome Page Works](02-how-it-works.md)
