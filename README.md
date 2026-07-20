# Ardhi University News Portal
### GROUP 1 — Django Templates: Building Dynamic Pages Using Django Templates

A small Django project built to demonstrate every topic in the assignment brief:

- What Django Templates are
- Django Template Language (DTL) — `{% %}` tags and `{{ }}` variables
- Template directories and configuration (`TEMPLATES` in `settings.py`, app `templates/` folder)
- Rendering templates using the `render()` function
- Passing data from views to templates (context dictionaries)
- Displaying variables
- Comments in templates (`{# ... #}`)

No database is used — all news data lives in a Python list of dictionaries
in `news/data.py`, as allowed by the assignment ("Database is Optional").

## Pages

| Page          | URL              | Template               |
|---------------|------------------|-------------------------|
| Home          | `/`              | `home.html`             |
| About         | `/about/`        | `about.html`            |
| Contact       | `/contact/`      | `contact.html`          |
| News listing  | `/news/`         | `news_list.html`        |
| News details  | `/news/<id>/`    | `news_detail.html`      |

All pages extend a shared `base.html`, which itself `{% include %}`s a
navbar and footer — showing template inheritance and reusable partials.

## Project structure

```
news_portal/
├── manage.py
├── news_portal/          # project settings, urls, wsgi
│   ├── settings.py       # TEMPLATES config lives here
│   ├── urls.py
│   └── wsgi.py
└── news/                 # the app
    ├── views.py          # every view calls render(request, template, context)
    ├── urls.py            # named URL patterns (news:home, news:news_detail, ...)
    ├── data.py            # in-memory news data (list of dicts) + helper functions
    ├── static/news/css/style.css
    └── templates/news/
        ├── base.html
        ├── includes/navbar.html
        ├── includes/footer.html
        ├── home.html
        ├── about.html
        ├── contact.html
        ├── news_list.html
        └── news_detail.html
```

## How to run it

1. Install Django (any recent 4.x/5.x version):
   ```
   pip install django
   ```
2. From the `news_portal/` folder, start the dev server:
   ```
   python manage.py runserver
   ```
3. Open http://127.0.0.1:8000/ in your browser.

No migrations are required to browse the site (no models/database are
used), but `python manage.py migrate` will still work fine if you want
the default admin tables set up.

## What to point out during the presentation

- **How Django locates templates**: `APP_DIRS: True` in `settings.py`
  makes Django search every installed app's `templates/` folder;
  `news/templates/news/...` is why templates are namespaced under `news/`.
- **How templates are rendered**: every function in `views.py` ends with
  `return render(request, "news/<template>.html", context)`.
- **How context data reaches templates**: the `context = {...}` dictionary
  built in each view becomes the `{{ variable }}` names available in
  that template (e.g. `latest_news`, `article`, `page_title`).
- **Live modification**: with `DEBUG = True` and the dev server running,
  edit any `.html` file and refresh the browser to see the change
  instantly — a good live demo of template rendering.
- **Common mistakes to show/discuss**: forgetting `{% load static %}`
  before using `{% static %}`, mismatched `{% endif %}` / `{% endfor %}`
  tags, referencing a context variable name that doesn't match the key
  used in the view, and forgetting to register a template's app in
  `INSTALLED_APPS`.
