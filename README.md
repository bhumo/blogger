# Blogger - A Django Blog Platform

Blogger is a web application built with Django that allows users to register, create, and read blog posts. It features category-based filtering, search functionality, and a clean user interface styled with Tailwind CSS.

## Features

*   **User Authentication:**
    *   User registration with custom fields (email, avatar, bio).
    *   Login and logout functionality.
    *   Password reset and change (via `django.contrib.auth.urls`).
*   **Blog Post Management:**
    *   Create new blog posts (requires login).
    *   Posts include title, content, and can be assigned to multiple categories.
    *   Author automatically assigned to the logged-in user.
*   **Blog Post Display:**
    *   Homepage listing all published blog posts, ordered by publication date.
    *   Pagination for blog posts.
    *   Filter posts by category.
    *   Search posts by title or content.
*   **Categories:**
    *   Dynamic category system.
    *   Categories are displayed and can be used for filtering.
*   **Comments:**
    *   Model for comments on blog posts (frontend/views for creating/displaying comments not yet fully implemented).
*   **Styling:**
    *   Frontend styled using Tailwind CSS.
    *   Select2 for enhanced multi-select dropdowns (e.g., for categories).
*   **Admin Interface:**
    *   Django admin interface for managing users, posts, categories, etc.
*   **Media Files:**
    *   Support for user avatar uploads.

## Project Structure

```
blogger/
├── blog/                 # Main application
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   │   ├── registration/
│   │   └── posts/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── blogsite/             # Django project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── media/                # For user-uploaded files (e.g., avatars)
├── templates/            # Project-level templates (e.g., base.html, home.html)
├── manage.py
└── README.md             # This file
```

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/bhumo/blogger.git
    cd blogger
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    (It's recommended to create a `requirements.txt` file)
    ```bash
    pip install Django Pillow # Add other dependencies if any
    # Example: pip install -r requirements.txt
    ```

4.  **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000/`. The admin panel will be at `http://120.0.0.1:8000/admin/`.

## Key Technologies Used

*   Python
*   Django
*   SQLite (default database)
*   HTML
*   Tailwind CSS
*   JavaScript (jQuery, Select2)

## Future Enhancements (Suggestions)

*   Implement full CRUD for comments.
*   User profile pages.
*   Edit/Delete functionality for blog posts.
*   Rich text editor for blog post content.
*   Deployment to a hosting platform.
*   More comprehensive unit and integration tests.