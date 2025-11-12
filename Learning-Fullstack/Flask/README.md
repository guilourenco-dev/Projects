# **Basic Flask Note-Taking Application**

This is a full-stack web application built with the Flask framework (Python) that allows users to register, log in, and manage a list of personal notes. This project serves as a foundational exercise in web development, covering user authentication, database management, and asynchronous operations (AJAX).

## **🚀 Features**

* **User Authentication:** Secure user registration, login, and logout implemented using Flask-Login and password hashing (werkzeug.security).  
* **Persistent Storage:** Notes and user data are stored in a relational database (database.db) managed via **Flask-SQLAlchemy**.  
* **CRUD Operations:** Users can Create (Add) and Delete notes in real-time.  
* **Responsive UI:** The front-end is styled using **Bootstrap 4** for a clean, responsive layout.  
* **Asynchronous Deletion:** Notes are deleted instantly without a full page reload using JavaScript's fetch API (AJAX).

## **⚙️ Technologies Used**

### **Backend**

* **Python 3**  
* **Flask:** Web framework for routing and serving content.  
* **Flask-SQLAlchemy:** ORM for database interaction (using SQLite).  
* **Flask-Login:** Session management and user authentication handling.  
* **werkzeug.security:** Used for hashing and verifying user passwords.

### **Frontend**

* **HTML / Jinja2:** Templating language for dynamic content generation.  
* **Bootstrap 4:** Primary CSS framework for styling.  
* **JavaScript:** Used for handling the asynchronous note deletion request.

## **📂 Project Structure**

The core application logic is organized within the website/ directory:

| File/Folder | Purpose |
| :---- | :---- |
| main.py | The main entry point to run the application. |
| website/\_\_init\_\_.py | Initializes the Flask application, configures the database, and registers Blueprints. |
| website/models.py | Defines the database structure: User and Note models. |
| website/auth.py | Handles all authentication routes (Login, Sign-Up, Logout). |
| website/views.py | Handles the main, logged-in content routes (Home page, Add Note, Delete Note). |
| website/templates/ | Contains the HTML templates (base.html, home.html, etc.). |
| website/static/ | Holds static assets like JavaScript (e.g., index.js). |

