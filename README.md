                                    ==================Machine Test====================

This is a Django-based REST API for managing users, clients, and projects within a project management system. The project includes CRUD operations for client and project entities and assigns users to projects.

===========================================================================================================================
Project Overview
The application supports:

User Management: Uses Django's built-in user management.
Client Management: API endpoints for registering, viewing, updating, and deleting clients.
Project Management: API endpoints for creating, assigning users, and retrieving projects for each client.
============================================================================================================================
The database used in this project is PostgreSQL (as specified in the requirements).

============================================================================================================================
Prerequisites
Python (>= 3.8)
Django (>= 4.0)
Django REST framework
MySQL or PostgreSQL
============================================================================================================================
Clone the repository:git clone https://github.com/mayurkosandar/Nimap_Infotech.git
cd your-repo-name
============================================================================================================================
Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
============================================================================================================================
Install dependencies:
pip install -r requirements.txt
============================================================================================================================
Set up the database:

Created a  PostgreSQL database and update your settings.py with the database credentials.
============================================================================================================================
Run migrations:

python manage.py makemigrations
python manage.py migrate
============================================================================================================================
Create a superuser to access the admin panel:- python manage.py createsuperuser
============================================================================================================================
Run the server:python manage.py runserver
============================================================================================================================
API Endpoints:-

Client Endpoints=
.List all clients: GET /clients/
.Create a new client: POST /clients/
.Retrieve a client with projects: GET /clients/<id>/
.Update client info: PUT/PATCH /clients/<id>/
.Delete a client: DELETE /clients/<id>/
============================================================================================================================

Project Endpoints
Create a new project (for a specific client): POST /clients/<client_id>/projects/
List all projects assigned to the logged-in user: GET /projects/

Example Requests:-POST /clients/
{
    "client_name": "Company A",
    "created_by": "username"
}
============================================================================================================================

Assign a Project
POST /clients/1/projects/
{
    "project_name": "Project Alpha",
    "users": [1, 2, 3]  // List of user IDs to be assigned
}
============================================================================================================================


