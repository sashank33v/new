# Smart Library Project Overview

## 1. Overview

This project is a Flask-based library web app for:

- viewing books
- adding new books
- showing total and available book counts
- storing data in `data.json`

The app is split into:

- `app.py` for routes and request handling
- `models/` for library and book logic
- `templates/` for UI rendering
- `data.json` for local persistence

## 2. Workflow

### Main Flow

1. User sends a request from the browser.
2. Flask route in `app.py` receives the request.
3. The `Library` object processes the action.
4. Book data is read from or written to `data.json`.
5. Flask passes results to the template.
6. HTML response is rendered in the browser.

### Flow Sheet

```text
User
  |
  v
Browser Request
  |
  v
Flask Route (app.py)
  |
  v
Library Object
  |
  +--> Create / read Book objects
  |
  +--> Read / write data.json
  |
  v
Jinja Template
  |
  v
Browser Response
```

## 3. OOP Concepts Applied

- Class and Object: `Library`, `Book`, `SimpleBook`, `User`, `Student`, and `Admin`
- Inheritance: `SimpleBook` inherits `Book`; `Student` and `Admin` inherit `User`
- Abstraction: `Book` and `User` use `ABC`, and `User.role()` is abstract
- Encapsulation: `title` is public, `_author` is protected, `__available` is private
- Composition: `Library` manages multiple book objects through `self.books`
- Class Method: `Book.get_total_books()` works on class-level state

## 4. Internal Data Workflow

### App Startup

```text
App starts
  |
  v
Library() created
  |
  v
load_books()
  |
  v
Read data.json
  |
  v
Create SimpleBook objects
  |
  v
Store in self.books
```

### Add Book Flow

```text
User submits add form
  |
  v
POST /add
  |
  v
request.form reads title and author
  |
  v
library.add_book(title, author)
  |
  v
SimpleBook object created
  |
  v
Append to self.books
  |
  v
save_books()
  |
  v
Write updated list to data.json
  |
  v
Redirect to /books
```

### View Books Flow

```text
GET /books or /
  |
  v
library.view_books()
  |
  v
available_books() when needed
  |
  v
Send data to template
  |
  v
Render page
```
