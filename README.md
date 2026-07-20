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
in `news/data.py`

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

1. Install Django :
   ```
   pip install django
   ```
2. From the `news_portal/` folder, start the dev server:
   ```
   python manage.py runserver
   ```
3. Open http://127.0.0.1:8000/ in your browser.

## GROUP MEMBERS
- BARIKI NSAJIGWA JOSEPH-32606/T.2024
- MARIA FRANCIS CHRISTIAN-34497/T.2024
- SHALOM PETER KOKONYO-34853/T.2024
- MECKZEDECK VEDASTUS BIDEBERI-32470/T.2024
- DAVID EDWARD KIGONI-34496/T.2024
- WITNES PASAKA SAMSON-33589/T.2024

