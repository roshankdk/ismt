# Django From Zero: Build Your First Blog App

This guide starts from **nothing** and ends with a working blog page in the browser.
Follow every step in order and don't skip any.

---

## What We Will Build

When you open `http://127.0.0.1:8000/blog/`, you will see:

> # Blog
> ## First Blog Post
> This is my first blog post.
> ## Second Blog Post
> This is my second blog post.
> ## Third Blog Post
> This is my third blog post.

---

## Table of Contents

- [Part 1: Setting Up Your Computer](#part-1-setting-up-your-computer)
  - [Step 1: Check Python](#step-1-check-python)
  - [Step 2: Create a Project Folder](#step-2-create-a-project-folder)
  - [Step 3: Create a Virtual Environment](#step-3-create-a-virtual-environment)
  - [Step 4: Install Django](#step-4-install-django)
- [Part 2: Creating the Django Project](#part-2-creating-the-django-project)
  - [Step 5: Create the Project](#step-5-create-the-project)
  - [Step 6: Run the Server for the First Time](#step-6-run-the-server-for-the-first-time)
- [Part 3: Creating the Blog App](#part-3-creating-the-blog-app)
  - [Step 7: Create the App](#step-7-create-the-app)
  - [Step 8: Register the App](#step-8-register-the-app)
  - [Step 9: Write the View](#step-9-write-the-view)
  - [Step 10: Create the Template](#step-10-create-the-template)
  - [Step 11: Create the App's urls.py](#step-11-create-the-apps-urlspy)
  - [Step 12: Connect the App to the Project](#step-12-connect-the-app-to-the-project)
  - [Step 13: See Your Blog](#step-13-see-your-blog)
- [Part 4: Understanding What We Built](#part-4-understanding-what-we-built)

---

# Part 1: Setting Up Your Computer

## Step 1: Check Python

Django is written in **Python**, so we need Python first.

Open the **Terminal** (Mac) or **Command Prompt** (Windows) and type:

**Mac:**
```bash
python3 --version
```

**Windows:**
```bash
python --version
```

You should see something like:

```
Python 3.14.7
```

> ❌ **No Python?** Download it from [python.org/downloads](https://www.python.org/downloads/).
> On Windows, tick **"Add Python to PATH"** during installation.

> 💡 In this guide:
> - **Mac** users type `python3`
> - **Windows** users type `python`
>
> After you turn on the virtual environment in Step 3, `python` works for everyone.

---

## Step 2: Create a Project Folder

Let's make a folder for our work and go inside it:

```bash
mkdir ismt_django
cd ismt_django
```

| Command | Meaning |
|---|---|
| `mkdir ismt_django` | **m**a**k**e a **dir**ectory (folder) called `ismt_django` |
| `cd ismt_django` | **c**hange **d**irectory: go inside the folder |

> 💡 Everything from now on happens **inside this folder**.

---

## Step 3: Create a Virtual Environment

### What is a virtual environment?

It's a **separate box** for this project's tools.
Anything we install goes into this box, not into the whole computer.
That way, different projects don't fight over different versions.

### Create it

**Mac:**
```bash
python3 -m venv venv
```

**Windows:**
```bash
python -m venv venv
```

👉 This makes a new folder called `venv`. That's our box.

### Turn it on (activate it)

**Mac:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

When it works, you'll see `(venv)` at the start of your terminal line:

```
(venv) ismt_django %
```

> ⚠️ **Important:** Every time you open a **new terminal**, you must activate `venv` again.
> If you don't see `(venv)`, it's not on.

> 💡 To turn it off later, type: `deactivate`

---

## Step 4: Install Django

With `(venv)` showing, type:

```bash
pip install django
```

`pip` is Python's tool for installing packages. It downloads Django into our `venv` box.

Check it worked:

```bash
python -m django --version
```

You should see a version number like:

```
6.1.2
```

---

# Part 2: Creating the Django Project

## Step 5: Create the Project

```bash
django-admin startproject weblinks_site .
```

> ⚠️ **Don't forget the dot `.` at the end!**
> The dot means "create it **here**, in this folder".
> Without it, Django makes an extra folder inside, which is confusing.

Now your folder looks like this:

```
ismt_django/
├── venv/
├── manage.py
└── weblinks_site/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

### What are these files?

| File | What it does |
|---|---|
| `manage.py` | Your **remote control**. You use it to run commands like `runserver` and `startapp` |
| `weblinks_site/` | The **project** folder: settings for the whole website |
| `settings.py` | The **rule book**: all the project's settings |
| `urls.py` | The **main reception desk**: decides where each URL goes |
| `__init__.py` | An empty file that tells Python "this folder is a package" |
| `asgi.py`, `wsgi.py` | Used when putting the website on a real server. **Ignore them for now** |

---

## Step 6: Run the Server for the First Time

```bash
python manage.py runserver
```

You'll see something like:

```
You have 18 unapplied migration(s). ...
Run 'python manage.py migrate' to apply them.

Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Open **http://127.0.0.1:8000/** in your browser.

🚀 You should see Django's **rocket page** with "The install worked successfully! Congratulations!"

| Part of the address | Meaning |
|---|---|
| `127.0.0.1` | "This computer" (also called `localhost`) |
| `8000` | The port number, like a room number |

### About the "unapplied migrations" message

Django has some built-in tables (for users, the admin panel and so on) that need to be created in the database.
Stop the server with `Ctrl + C`, then run:

```bash
python manage.py migrate
```

👉 This creates a file called `db.sqlite3`. That's our database.
Run the server again, and the warning is gone:

```bash
python manage.py runserver
```

> 💡 Keep the server running in **one terminal**.
> Open a **second terminal** (and activate `venv` there too) for the other commands.

---

# Part 3: Creating the Blog App

### Project vs App

| | Meaning | Example |
|---|---|---|
| **Project** | The **whole website** | `weblinks_site` |
| **App** | **One part** of the website, doing one job | `blog`, `shop`, `accounts` |

One project can have **many apps**. Let's make our first one: `blog`.

---

## Step 7: Create the App

```bash
python manage.py startapp blog
```

A new `blog` folder appears:

```
blog/
├── __init__.py
├── admin.py
├── apps.py
├── migrations/
│   └── __init__.py
├── models.py
├── tests.py
└── views.py
```

| File | What it does |
|---|---|
| `views.py` | **Python functions that return pages.** We'll write code here ✍️ |
| `models.py` | Database tables (a later lesson) |
| `admin.py` | Shows models in the admin panel (a later lesson) |
| `apps.py` | The app's settings. Leave it as it is |
| `migrations/` | Database change history. Leave it as it is |
| `tests.py` | Tests for the app (a later lesson) |

---

## Step 8: Register the App

Django doesn't know about our new app yet. We have to tell it.

Open `weblinks_site/settings.py`, find `INSTALLED_APPS`, and add `'blog'` at the end:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',          # 👈 our new app
]
```

> ⚠️ Don't forget the **comma** `,` after `'blog'` and the quotes around it.

---

## Step 9: Write the View

A **view** is a Python function. It gets a **request** from the browser and sends back a **page**.

Open `blog/views.py` and replace everything with:

```python
from django.shortcuts import render

def blog_list(request):
    posts = [
        {'title': 'First Blog Post', 'content': 'This is my first blog post.'},
        {'title': 'Second Blog Post', 'content': 'This is my second blog post.'},
        {'title': 'Third Blog Post', 'content': 'This is my third blog post.'},
    ]
    return render(request, 'blog_list.html', {'posts': posts})
```

### Line by line

| Code | Meaning |
|---|---|
| `from django.shortcuts import render` | Brings in `render`, which turns an HTML file into a web page |
| `def blog_list(request):` | A function called `blog_list`. **Every view gets `request`** |
| `posts = [ ... ]` | A **list** of blog posts. Each post is a **dictionary** with a `title` and `content` |
| `return render(...)` | Sends the page back to the browser |

### Understanding `render()`

```python
render(request, 'blog_list.html', {'posts': posts})
#        ①            ②                  ③
```

| Part | Meaning |
|---|---|
| ① `request` | The browser's request. Always pass it first |
| ② `'blog_list.html'` | Which HTML file to show |
| ③ `{'posts': posts}` | The **data** we send to the HTML. This is called the **context** |

### What is the context?

It's like a **delivery box** from Python to HTML 📦

```python
{'posts': posts}
#  ▲        ▲
#  │        └── the Python list we made above
#  └── the name the HTML file will use
```

The HTML can now use the word `posts` to get our list.

> 💡 For now, our posts are written directly in Python.
> In a later lesson we'll get them from a **database** instead.

---

## Step 10: Create the Template

A **template** is an HTML file that can show data from Python.

1. Inside the `blog` folder, make a new folder called **`templates`**
2. Inside `templates`, make a new file called **`blog_list.html`**

```
blog/
└── templates/
    └── blog_list.html
```

> ⚠️ The folder name must be exactly **`templates`** (with an **s**).

Write this in `blog/templates/blog_list.html`:

```html
<!DOCTYPE html>
<html>
<head><title>Blog</title></head>
<body>
  <h1>Blog</h1>
  {% for post in posts %}
    <h2>{{ post.title }}</h2>
    <p>{{ post.content }}</p>
    <hr>
  {% endfor %}
</body>
</html>
```

### Django template language

Normal HTML can't loop over data, but Django adds two special kinds of tags:

| Syntax | Name | What it does | Remember it as |
|---|---|---|---|
| `{{ ... }}` | **Variable** | **Shows** a value on the page | Double curly = **display** |
| `{% ... %}` | **Tag** | **Does** something, like a loop | Curly + percent = **logic** |

### Understanding the loop

```html
{% for post in posts %}        ← start: take each post from the list, one by one
    <h2>{{ post.title }}</h2>  ← show this post's title
    <p>{{ post.content }}</p>  ← show this post's content
    <hr>                       ← a line between posts
{% endfor %}                   ← end of the loop
```

It works just like a Python `for` loop:

| Python | Django template |
|---|---|
| `for post in posts:` | `{% for post in posts %}` |
| `print(post['title'])` | `{{ post.title }}` |
| (indentation ends the loop) | `{% endfor %}` |

> ⚠️ Every `{% for %}` **must** have an `{% endfor %}`.

> 💡 In Python we write `post['title']`, but in templates we write `post.title` with a **dot**.

Since there are 3 posts, the loop runs **3 times** and makes 3 headings and 3 paragraphs.

---

## Step 11: Create the App's urls.py

`startapp` doesn't make a `urls.py`, so we create it ourselves.

Create a new file `blog/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
]
```

### Line by line

| Code | Meaning |
|---|---|
| `from django.urls import path` | Brings in `path` to make URL rules |
| `from . import views` | The `.` means **"this same folder"**, so this imports `blog/views.py` |
| `urlpatterns = [ ... ]` | The list of URL rules. Django looks for this exact name |
| `''` | An empty path: the **main page of this app** |
| `views.blog_list` | The view function to run |
| `name='blog_list'` | A **nickname** for this URL, so we can use it elsewhere later |

> ⚠️ Write `views.blog_list`, **not** `views.blog_list()`.
> We're giving Django the function to run later, not running it now.

---

## Step 12: Connect the App to the Project

The project's `urls.py` is the **main reception desk**. We need to tell it to send blog visitors to the blog app.

Open `weblinks_site/urls.py` and change it to:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
```

| Code | Meaning |
|---|---|
| `include` | Added to the import. We need it to connect the app |
| `path('blog/', include('blog.urls'))` | Any URL starting with `blog/` is sent to `blog/urls.py` |

### How the URLs join together

| Project urls.py | + | App urls.py | = | Full address |
|---|---|---|---|---|
| `'blog/'` | + | `''` | = | `/blog/` ✅ |

---

## Step 13: See Your Blog

Make sure the server is running:

```bash
python manage.py runserver
```

Open **http://127.0.0.1:8000/blog/** in your browser 🎉

You should see the **Blog** heading and **three blog posts**.

> 💡 If you open `http://127.0.0.1:8000/` now, you'll see a **404 Page not found**.
> That's normal, because we didn't make a page for `/`.
> The 404 page lists all the URLs Django knows, which is handy for checking your work.

---

# Part 4: Understanding What We Built

## The Journey of a Request

```
You type: http://127.0.0.1:8000/blog/
                │
                ▼
   settings.py ──────► ROOT_URLCONF = 'weblinks_site.urls'
                │      "Start with the project's urls.py"
                ▼
   weblinks_site/urls.py ──► path('blog/', include('blog.urls'))
                │            "blog/? Send it to the blog app"
                ▼
   blog/urls.py ──────► path('', views.blog_list)
                │       "The empty path? Run blog_list"
                ▼
   blog/views.py ─────► def blog_list(request):
                │           posts = [...]
                │           return render(request, 'blog_list.html', {'posts': posts})
                │       "Here's the data, put it in the HTML"
                ▼
   blog/templates/blog_list.html ──► {% for post in posts %} ...
                │                     "Loop and show each post"
                ▼
           🖥️  Browser shows the blog!
```

## The Restaurant Example 🍽️

| Restaurant | Django | Our file |
|---|---|---|
| The customer asks for food | The **browser** asks for a page | — |
| The reception desk sends you to a section | The **project urls.py** | `weblinks_site/urls.py` |
| The section's waiter takes your order | The **app urls.py** | `blog/urls.py` |
| The cook prepares the food | The **view** | `blog/views.py` |
| The ingredients | The **context** (data) | `{'posts': posts}` |
| The plate the food is served on | The **template** | `blog/templates/blog_list.html` |

## How Django Found `blog_list.html`

When the view says `render(request, 'blog_list.html', ...)`, Django:

1. Looks at `INSTALLED_APPS` → finds `'blog'`
2. Sees `'APP_DIRS': True` in `TEMPLATES` (in `settings.py`) → looks inside `blog/templates/`
3. Finds `blog_list.html` ✅

That's why we needed **both** Step 8 (register the app) **and** a folder named exactly `templates`.

## Final Folder Structure

```
ismt_django/
├── venv/                    ← virtual environment (don't touch)
├── db.sqlite3               ← database (made by migrate)
├── manage.py                ← remote control
├── weblinks_site/           ← PROJECT
│   ├── settings.py          ← ✏️ added 'blog'
│   └── urls.py              ← ✏️ added include('blog.urls')
└── blog/                    ← APP
    ├── views.py             ← ✏️ blog_list view
    ├── urls.py              ← 🆕 new file
    └── templates/           ← 🆕 new folder
        └── blog_list.html   ← 🆕 new file
```

## All Commands Used

| Command | What it does |
|---|---|
| `python3 -m venv venv` | Creates the virtual environment |
| `source venv/bin/activate` (Mac)<br>`venv\Scripts\activate` (Windows) | Turns on the virtual environment |
| `pip install django` | Installs Django |
| `python -m django --version` | Shows the Django version |
| `django-admin startproject weblinks_site .` | Creates the project |
| `python manage.py runserver` | Starts the website |
| `python manage.py migrate` | Sets up the database |
| `python manage.py startapp blog` | Creates an app |
| `Ctrl + C` | Stops the server |
| `deactivate` | Turns off the virtual environment |

## Words to Remember

| Word | One-line meaning |
|---|---|
| **Virtual environment** | A separate box for one project's tools |
| **Project** | The whole website |
| **App** | One part of the website |
| **URL** | The address that decides which view runs |
| **View** | A Python function that returns a page |
| **Template** | An HTML file that can show Python data |
| **Context** | The data (a dictionary) sent from the view to the template |
| `{{ }}` | Shows a value |
| `{% %}` | Runs logic, like a loop |

---

## Common Mistakes

| Error you see | What to check |
|---|---|
| `zsh: command not found: python` | On Mac, use `python3`, or activate `venv` first |
| `django-admin: command not found` | Is `venv` active? Do you see `(venv)`? Did you run `pip install django`? |
| `No module named django` | Activate `venv` first |
| `TemplateDoesNotExist at /blog/` | Is the folder named `templates` (with an **s**)? Is it **inside** `blog/`? Is `'blog'` in `INSTALLED_APPS`? |
| `ModuleNotFoundError: No module named 'blog.urls'` | Did you create `blog/urls.py`? Check the spelling |
| `NameError: name 'include' is not defined` | Change the import to `from django.urls import path, include` |
| `Page not found (404)` | Are you opening `/blog/` and not just `/`? |
| Page shows the heading but no posts | Does the context say `{'posts': posts}`? Does the template say `posts` (same spelling)? |
| `TemplateSyntaxError ... endfor` | Every `{% for %}` needs an `{% endfor %}` |
| `That port is already in use` | A server is already running in another terminal. Stop it with `Ctrl + C` |
| Changes don't show | Save the file, then refresh the browser |

---

## Practice Tasks

### 🟢 Easy
1. Add a **fourth** blog post to the list in `views.py`.
2. Change the `<h1>` from `Blog` to `My Blog`.

### 🟡 Medium
3. Add an `author` to each post, like `'author': 'Ram'`, and show it in the template using `{{ post.author }}`.
4. Add a `date` to each post and show it under the title.

### 🔴 Challenge
5. Make an **About** page at `http://127.0.0.1:8000/blog/about/`.
   - Hint 1: Make `blog/templates/about.html`
   - Hint 2: Add an `about` view in `blog/views.py`
   - Hint 3: Add `path('about/', views.about, name='about')` to `blog/urls.py`

---

## Quick Quiz

1. Why do we use a virtual environment?
2. What does the `.` at the end of `django-admin startproject weblinks_site .` mean?
3. What's the difference between a project and an app?
4. What is the third argument in `render(request, 'blog_list.html', {'posts': posts})` called?
5. What is the difference between `{{ }}` and `{% %}`?
6. The project has `path('blog/', ...)` and the app has `path('', ...)`. What is the full URL?

<details>
<summary>Answers</summary>

1. To keep this project's tools (like Django) in a separate box, so they don't mix with other projects.
2. Create the project **in the current folder**, without making an extra folder.
3. A project is the whole website. An app is one part of it.
4. The **context**: the data sent from the view to the template.
5. `{{ }}` **shows** a value. `{% %}` **does** something, like a loop.
6. `/blog/`

</details>
