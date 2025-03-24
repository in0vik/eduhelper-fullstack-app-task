## Project strucutre

Below is a detailed overview of each file and folder in this project. You can use it to understand the project’s layout and what each file does. Feel free to **update** or **expand** this document with anything new you add or change!

```
└── eduhelper-fullstack-app/
    ├── app/
    │   ├── migrations/
    │   │   ├── __init__.py
    │   │   └── 0001_initial.py
    │   ├── templates/
    │   │   └── home.html
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── models.py
    │   ├── urls.py
    │   └── views.py
    ├── static/
    │   ├── css/
    │   │   └── style.css
    │   └── js/
    │       └── script.js
    ├── eduhelper_project/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    └── README_for_students.md
```

### Folders and Files

1. **`app/`**  
   - Holds everything specific to our Django app (models, views, templates, etc.).

2. **`app/migrations/`**  
   - Auto-generated files that track changes to the database schema.  
   - **`__init__.py`**: Tells Python this folder is a package.  
   - **`0001_initial.py`**: The first migration that creates our `SavedAnswer` model table.

3. **`app/templates/home.html`**  
   - Main HTML template for our Q&A page. It uses Django templating features (e.g., `{{ saved_answers }}`).

4. **`app/__init__.py`**  
   - Makes the `app` folder a Python package.

5. **`app/admin.py`**  
   - Registers the `SavedAnswer` model with the Django admin site, so we can view/edit data in the admin panel.

6. **`app/models.py`**  
   - Contains the Django **`SavedAnswer`** model (which has `question`, `answer`, and `created_at` fields).

7. **`app/urls.py`**  
   - Defines the URL patterns for the `app` (like `"/"` for the home page, `"/ask/"` for asking a question, etc.).

8. **`app/views.py`**  
   - Contains the **logic** for handling requests.  
   - `home()` shows the homepage and saved Q&As.  
   - `ask_question()` integrates with the **Gemini API** to generate an answer.  
   - `save_answer()` saves Q&A to the database.

9. **`static/css/style.css`**  
   - Custom stylesheet for the project. Adjust colors, layout, etc.

10. **`static/js/script.js`**  
    - JavaScript file that handles front-end interactions:
      - Submits questions via AJAX.  
      - Displays answers.  
      - Saves answers to the server.

11. **`eduhelper_project/`**  
    - The root configuration folder for the Django project.

12. **`eduhelper_project/asgi.py`** and **`eduhelper_project/wsgi.py`**  
    - Configuration files for deploying Django with ASGI or WSGI servers. Usually, you don’t touch these often.

13. **`eduhelper_project/settings.py`**  
    - Django’s main settings (database config, installed apps, static files, etc.).

14. **`eduhelper_project/urls.py`**  
    - Routes top-level URLs to different apps’ `urls.py`. Includes the admin route.

15. **`manage.py`**  
    - Django’s command-line utility (runserver, migrations, shell, etc.).

---

### Tips & Reminders

- If you add a new Django app, remember to **include** it in `INSTALLED_APPS` inside `settings.py`.
- Migrations get automatically generated with `python manage.py makemigrations`, and then you apply them with `python manage.py migrate`.
- Any new static files you add should go into `static/` (or a subfolder within it) so Django knows where to find them.
