# How the Welcome Page Works

In [Lesson 1](01-welcome-page.md) we built a page that shows **Welcome to Django World**.
Now let's understand **every file and every line** we used, in the order Django uses them.

---

## The Big Picture

```
You type: http://127.0.0.1:8000/hello/
                    │
                    ▼
   ① settings.py         "Which urls.py should I check first?"
                    │
                    ▼
   ② Project urls.py     "Which app handles this?"
                    │
                    ▼
   ③ App urls.py         "Which view handles this?"
                    │
                    ▼
   ④ views.py            "Run the function and get the page"
                    │
                    ▼
   ⑤ index.html          "This is the page"
                    │
                    ▼
   Browser shows: Welcome to Django World
```

### A Restaurant Example

| Restaurant                                  | Django                          | Our file                    |
|---------------------------------------------|---------------------------------|-----------------------------|
| You (the customer) ask for food             | The **browser** asks for a page | —                           |
| The reception desk sends you to a section   | The **project urls.py**         | `weblinks_site/urls.py`     |
| The section's waiter takes your order       | The **app urls.py**             | `home/urls.py`              |
| The cook makes the food                     | The **view**                    | `home/views.py`             |
| The plate of food you get                   | The **template (HTML)**         | `home/templates/index.html` |

---

## ① settings.py: The Rule Book

Before anything else, Django reads `weblinks_site/settings.py`.
Three settings matter for our page:

```python
INSTALLED_APPS = [
    ...
    'home',
]
```
👉 This tells Django that a `home` app exists. Without this line, Django won't look inside `home/` for templates.

```python
ROOT_URLCONF = 'weblinks_site.urls'
```
👉 This tells Django that the **first** URL file to check is `weblinks_site/urls.py`.
That's why it's called the **project urls.py**.

```python
'APP_DIRS': True,
```
👉 This tells Django to look for HTML files inside each app's `templates` folder.

---

## ② Project urls.py: The Main Reception Desk

**File:** `weblinks_site/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]
```

### Line by line

| Code                                     | Meaning                                                                 |
|------------------------------------------|-------------------------------------------------------------------------|
| `from django.contrib import admin`       | Brings in Django's built-in admin panel                                 |
| `from django.urls import path, include`  | Brings in two tools: `path` (makes a URL rule) and `include` (sends URLs to an app) |
| `urlpatterns = [ ... ]`                  | A **list** of URL rules. Django checks them **from top to bottom**      |
| `path('admin/', admin.site.urls)`        | If the URL starts with `admin/`, open the admin panel                   |
| `path('', include('home.urls'))`         | For anything else, go check `home/urls.py`                              |

### What is `path()`?

```python
path( 'the URL' , 'what to do' )
```
It's a rule that says: "if the URL looks like **this**, do **that**."

### What is `include()`?

It means **"I don't handle this myself. Ask the app's urls.py."**
The reception desk doesn't serve customers itself. It only sends them to the right section.

---

## ③ App urls.py: The App's Own Desk

**File:** `home/urls.py` (we created this file ourselves; `startapp` doesn't make it)

```python
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.index),
]
```

### Line by line

| Code                           | Meaning                                                                  |
|--------------------------------|--------------------------------------------------------------------------|
| `from django.urls import path` | We need `path` to write URL rules                                        |
| `from . import views`          | The `.` means **"this same folder"**, so this imports `home/views.py`    |
| `path('hello/', views.index)`  | If the URL is `hello/`, run the `index` function from `views.py`         |

> ⚠️ Write `views.index`, **not** `views.index()`.
> We are *giving Django the function* so it can run it later.
> We are not running it ourselves.

### How the two URL files join together

Django **adds** the project part and the app part together:

| Project urls.py | + | App urls.py | = | Full URL     |
|-----------------|---|-------------|---|--------------|
| `''`            | + | `'hello/'`  | = | `/hello/` ✅ |

If the project had `path('home/', include('home.urls'))`,
the page would be at `/home/hello/` instead.

### Why two urls.py files?

Think of a big school:

- The **main office** (project `urls.py`) doesn't teach. It only tells you which department to go to.
- Each **department** (app `urls.py`) knows its own classrooms.

When the website grows and gets more apps (like `blog` or `shop`),
each app looks after its own URLs, and the project stays neat.

---

## ④ views.py: The Cook

**File:** `home/views.py`

```python
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
```

### Line by line

| Code                                     | Meaning                                                                |
|------------------------------------------|------------------------------------------------------------------------|
| `from django.shortcuts import render`    | Brings in `render`, a helper that turns an HTML file into a web page   |
| `def index(request):`                    | A normal Python function called `index`. **Every view gets `request`** |
| `return render(request, 'index.html')`   | Finds `index.html` and sends it back to the browser                    |

### What is a view?

A view is **just a Python function** that:

1. **Takes** a request (what the browser asked for)
2. **Returns** a response (the page to show)

### What is `request`?

It's a package of information from the browser, such as:

- Which URL was asked for: `request.path` → `/hello/`
- Which method was used: `request.method` → `GET`
- Which user is logged in: `request.user`

Django creates it and passes it to your view automatically.

### What does `render()` do?

```python
render( request , 'which HTML file' )
```
It looks for the HTML file, reads it, and wraps it in a **response** for the browser.

---

## ⑤ The Template: The Final Page

**File:** `home/templates/index.html`

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

| Tag               | Meaning                                     |
|-------------------|---------------------------------------------|
| `<!DOCTYPE html>` | Tells the browser this is an HTML page      |
| `<title>`         | The text on the **browser tab**             |
| `<h1>`            | The big heading on the page                 |

### How did Django find this file?

When the view says `render(request, 'index.html')`, Django:

1. Checks `INSTALLED_APPS` → finds `home`
2. Sees `APP_DIRS: True` → looks in `home/templates/`
3. Finds `index.html` ✅

That's why the folder **must** be called `templates` (with an **s**).

---

## ⑥ Running It: manage.py runserver

```bash
python manage.py runserver
```

👉 This starts a small web server on your computer at `http://127.0.0.1:8000/`.

- `127.0.0.1` means "this computer"
- `8000` is the port number (like a room number)

It keeps running, and when you save a file it restarts by itself.
To stop it, press `Ctrl + C`.

---

## What Happens With Different URLs?

| You open  | What happens                                                    | Result                |
|-----------|-----------------------------------------------------------------|-----------------------|
| `/hello/` | Project → `home.urls` → `hello/` matches → `index` view         | ✅ Welcome page       |
| `/admin/` | Project → `admin/` matches                                      | ✅ Admin login        |
| `/`       | Project → `home.urls` → nothing matches `''`                    | ❌ 404 Page not found |
| `/abc/`   | No rule matches                                                 | ❌ 404 Page not found |

> 💡 Because `DEBUG = True` in `settings.py`, the 404 page lists
> **all the URLs Django knows about**. That's very helpful when you get lost.

---

## The Whole Thing in One Picture

```
http://127.0.0.1:8000/hello/
            │
            ▼
settings.py ──► ROOT_URLCONF = 'weblinks_site.urls'
            │
            ▼
weblinks_site/urls.py ──► path('', include('home.urls'))
            │
            ▼
home/urls.py ──► path('hello/', views.index)
            │
            ▼
home/views.py ──► def index(request):
                      return render(request, 'index.html')
            │
            ▼
home/templates/index.html ──► <h1>Welcome to Django World</h1>
            │
            ▼
        🖥️  Browser
```

---

## 5 Words to Remember

| Word         | One-line meaning                               |
|--------------|------------------------------------------------|
| **Project**  | The whole website (`weblinks_site`)            |
| **App**      | One part of the website (`home`)               |
| **URL**      | The address that decides which view runs       |
| **View**     | A Python function that returns a page          |
| **Template** | The HTML file the user sees                    |

---

## Quick Quiz

1. Which setting tells Django which `urls.py` to check first?
2. What does `include('home.urls')` do?
3. Why do we write `views.index` and not `views.index()`?
4. If the project URL is `'shop/'` and the app URL is `'items/'`, what is the full URL?
5. Where does Django look for `index.html`?

<details>
<summary>Answers</summary>

1. `ROOT_URLCONF`
2. It sends the URL to the `home` app's `urls.py` to handle.
3. We give Django the function to run later. We don't run it ourselves.
4. `/shop/items/`
5. In `home/templates/`, because `home` is in `INSTALLED_APPS` and `APP_DIRS` is `True`.

</details>
