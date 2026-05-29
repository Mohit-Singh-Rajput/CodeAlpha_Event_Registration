# CodeAlpha Event Registration System 🎟️

A robust, relational web application built with Django that allows users to view upcoming events and seamlessly register for them. This system leverages Django's built-in Object-Relational Mapper (ORM) and authentication framework to securely manage user data and prevent duplicate registrations.

Developed as Task 2 for the CodeAlpha Backend Development Internship.

## 🛠️ Tech Stack
* **Backend Framework:** Python, Django
* **Database:** SQLite (Built-in)
* **Frontend:** HTML, CSS (Django Templates)
* **Authentication:** Django `contrib.auth`

## ✨ Core Features
* **Relational Database Architecture:** Utilizes Django Models to establish distinct `Event` and `Registration` tables, connected via Foreign Keys to ensure data integrity.
* **Master Admin Dashboard:** Fully integrated with Django's admin interface for easy creation, editing, and deletion of events.
* **Secure Registration Logic:** Implements `@login_required` decorators to restrict access and utilizes `get_or_create` logic to prevent users from registering for the same event twice.
* **Dynamic Frontend Rendering:** Uses Django Template tags and context dictionaries to dynamically inject database records directly into the HTML UI.

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Mohit-Singh-Rajput/CodeAlpha_Event_Registration.git](https://github.com/Mohit-Singh-Rajput/CodeAlpha_Event_Registration.git)
   cd CodeAlpha_Event_Registration

2. **Set up a virtual environment:**
   python -m venv venv
   venv\Scripts\activate  # On Windows

3. **Install the dependencies:**
   pip install django

4. **Initialize the database:**
   python manage.py makemigrations
   python manage.py migrate

5. **Create an admin account:**
   python manage.py createsuperuser

6. **Start the server:**
   python manage.py runserver

7. **Access the application:** Public View: http://127.0.0.1:8000/
   Admin Dashboard: http://127.0.0.1:8000/admin/
