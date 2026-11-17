# Blog Project Plan: What We Are Going to Build

In the last guide we made a blog page with 3 **hardcoded** posts.
In this project we turn it into a **real blog**: posts live in a database, **anyone can read**,
and **logged-in users** can write, edit and delete their own posts.

**Time budget:** about 8 hours, split into days.

---

## 1. The Golden Rule

| Visitor type | Can do |
|--------------|--------|
| **Free visitor (not logged in)** | Read the list, open any post, search, filter by category |
| **Logged-in user** | Everything above **+ create** posts |
| **Author of a post** | Everything above **+ edit and delete** that post |

> Login is needed **only** to create, edit or delete. Reading is always free.

---

## 2. Features

| # | Feature | Who | Day |
|---|---------|-----|-----|
| 1 | Posts stored in a database | - | 1 |
| 2 | Categories | - | 1 |
| 3 | Public post list | Everyone | 1 |
| 4 | Public post detail page (`/blog/post/my-post/`) | Everyone | 1 |
| 5 | Admin panel | Superuser | 1 |
| 6 | Search, category filter, pagination | Everyone | 2 |
| 7 | Register / Login / Logout | Everyone | 2 |
| 8 | Create a post | Logged-in | 2 |
| 9 | Edit / Delete a post | Author only | 2 |
| 10 | My posts page | Logged-in | 2 |
| 11 | Anonymous comments (name + text) *(optional)* | Everyone | stretch |

---

## 3. The Big Picture: How a Request Flows

```mermaid
flowchart LR
    A[Browser] -->|1. asks for /blog/| B[urls.py]
    B -->|2. finds the matching view| C[views.py]
    C -->|3. asks for data| D[(models.py / Database)]
    D -->|4. returns posts| C
    C -->|5. sends data to| E[Template .html]
    E -->|6. HTML page| A
```

**In one line:** URL -> View -> Model -> Template -> Browser.

---

## 4. The User Journey

```mermaid
flowchart TD
    Start([Anyone opens /blog/]) --> List[See list of posts]
    List --> Search[Search or filter by category]
    List --> Detail[Open a post and read it]
    List --> Write{Wants to write a post?}
    Write -->|Not logged in| Login[Login or Register]
    Login --> Create
    Write -->|Logged in| Create[Create a post]
    Create --> Detail
    Detail --> Own{Is this my post?}
    Own -->|Yes, logged in| Edit[Edit or Delete]
    Own -->|No| List
    Edit --> List
```

---

## 5. Database Design (Models)

```mermaid
erDiagram
    USER ||--o{ POST : writes
    CATEGORY ||--o{ POST : groups
    POST ||--o{ COMMENT : "has (optional)"

    USER {
        int id
        string username
        string password
    }
    CATEGORY {
        int id
        string name
        string slug
    }
    POST {
        int id
        string title
        string slug
        text content
        bool published
        datetime created_at
        datetime updated_at
        int author_id
        int category_id
    }
    COMMENT {
        int id
        string name
        text body
        datetime created_at
        int post_id
    }
```

- `USER` is Django's built-in model (we do not write it).
- One user has many posts. One category has many posts.
- `COMMENT` is optional (stretch goal). It has a `name` field because commenters are not logged in.

---

## 6. Pages and URLs

| URL | What it does | Who can open it |
|-----|--------------|-----------------|
| `/blog/` | Post list (search, filter, pages on Day 2) | **Everyone** |
| `/blog/post/<slug>/` | Post detail | **Everyone** |
| `/blog/new/` | Create post | Logged-in users |
| `/blog/post/<slug>/edit/` | Edit post | Author only |
| `/blog/post/<slug>/delete/` | Delete post | Author only |
| `/blog/mine/` | My posts | Logged-in users |
| `/blog/register/` | Sign up | Everyone |
| `/blog/login/`, `/blog/logout/` | Login, logout | Everyone |
| `/admin/` | Admin panel | Superuser |

---

## 7. Permission Rules (Quick Reference)

```mermaid
flowchart TD
    R[Request arrives] --> W{Create, edit or delete?}
    W -->|No, just reading| Free[Allowed for everyone]
    W -->|Yes| L{Logged in?}
    L -->|No| Redirect[Redirect to login page]
    L -->|Yes| A{Creating a new post?}
    A -->|Yes| OK[Allowed]
    A -->|No: edit or delete| O{Is the post theirs?}
    O -->|Yes| OK
    O -->|No| Block[Blocked: 403 Forbidden]
```

---

## 8. Files We Will Touch

```mermaid
flowchart TD
    P[blogsite/] --> S[settings.py: login redirects on Day 2]
    P --> U[urls.py: already includes blog.urls]
    B[blog/] --> M[models.py: Category, Post]
    B --> F[forms.py: PostForm, RegisterForm on Day 2]
    B --> V[views.py: list, detail, then create/edit/delete]
    B --> BU[urls.py: routes]
    B --> A[admin.py: register models]
    B --> T[templates/blog/: base, list, detail, form, login, register]
```

---

## 9. Build Order

```mermaid
flowchart LR
    subgraph Day 1: Public blog
    S1[1. Models and migrations] --> S2[2. Admin and sample data]
    S2 --> S3[3. Base template]
    S3 --> S4[4. Post list from DB]
    S4 --> S5[5. Post detail]
    end
    subgraph Day 2: Write access
    S6[6. Search, filter, pagination] --> S7[7. Register, login, logout]
    S7 --> S8[8. Create, edit, delete with permissions]
    S8 --> S9[9. Testing and polish]
    end
    S5 --> S6
```

| Step | What you learn |
|------|----------------|
| 1. Models | `models.Model`, fields, `ForeignKey`, `makemigrations`, `migrate` |
| 2. Admin | `admin.site.register`, `createsuperuser` |
| 3. Base template | `{% extends %}`, `{% block %}` |
| 4. List page | `{% for %}`, ORM queries, `{% url %}` |
| 5. Detail page | Slugs, `get_object_or_404` |
| 6. Search | `Q` objects, `request.GET`, `paginate_by` |
| 7. Auth | Built-in `LoginView`, `UserCreationForm`, `{% if user.is_authenticated %}` |
| 8. CRUD | `ModelForm`, `CreateView`, `UpdateView`, `DeleteView`, `LoginRequiredMixin` |
| 9. Testing | Manual click-through, `tests.py` basics |

---

## 10. Out of Scope (Stretch Goals)

- Anonymous comments
- Image upload for posts (needs Pillow and media settings)
- Likes, tags, user profiles
- Bootstrap styling
- Deploying the site

---

## 11. Done Checklist

- [ ] A visitor who is **not logged in** can read the list and any post
- [ ] Can register, log in and log out
- [ ] Not-logged-in visitors are sent to login when they open `/blog/new/`
- [ ] Can create a post and see it in the list
- [ ] Can edit and delete my own post
- [ ] Cannot edit or delete someone else's post
- [ ] Search and category filter work
- [ ] Pagination appears with more than 5 posts
- [ ] Admin panel shows all models
