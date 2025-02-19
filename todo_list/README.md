# To-Do List Using Django

This is a simple To-Do List application built using Django. It allows users to add and delete tasks.

## Features

- Add new tasks
- Delete existing tasks
- View all tasks

## Project Structure

```
todo_list/
├── tasks/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── todo_list/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/
│   └── styles.css
├── templates/
│   └── task_list.html
├── manage.py
└── .gitignore
```

## Requirements

- Python 3.x
- Django 4.2.3

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd todo_list
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py migrate
    ```

## Running the Project

1. Start the development server:
    ```sh
    python manage.py runserver
    ```

2. Open your web browser and go to `http://127.0.0.1:8000/` to see the application.

## Usage

- To add a new task, enter the task name in the input field and click the "+" button.
- To delete a task, click the "Delete" link next to the task.

## License

This project is licensed under the MIT License.