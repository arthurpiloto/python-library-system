# Python Library Management System (CLI)

A comprehensive command-line interface (CLI) application for managing a library system, built entirely in Python. This project was designed to apply and demonstrate core Object-Oriented Programming (OOP) principles within a clean Model-View-Controller (MVC) architecture.

## Features

- **Full CRUD Operations:** Create, Read, Update, and Delete for all core entities:
  - Books
  - Readers
  - Authors
  - Genres
- **Advanced Loan Management:**
  - Individual loans for each book, allowing for separate due dates.
  - A reader is limited to a maximum of 3 active loans.
- **Inventory Control:**
  - Books have a specific number of available copies.
  - A loan is only possible if a copy is available.
- **Reservation System:**
  - Readers can join a waiting queue for a book that is currently unavailable.
- **Clean Architecture:**
  - **Model:** A rich domain model where classes (Book, Reader) contain their own business logic (`is_available`, `can_loan`).
  - **View:** The `ConsoleView` is a "dumb" component, responsible only for displaying information and capturing user input.
  - **Controller:** The `LibraryController` orchestrates the application flow, connecting the user's actions from the View to the business logic in the Model.
  - **Persistence:** A fast, in-memory database simulation using Python dictionaries for O(1) lookups.

## Project Structure

The project follows a standard, modular Python package structure:

```bash
library_management_system/
├── library/
│ ├── init.py
│ ├── controller/
│ │ ├── init.py
│ │ └── library_controller.py
│ ├── model/
│ │ ├── init.py
│ │ └── (author.py, book.py, reader.py, ...)
│ ├── persistence/
│ │ ├── init.py
│ │ └── (database.py, repository.py)
│ └── view/
│ ├── init.py
│ └── console_view.py
├── .gitignore
├── LICENSE
├── main.py
└── README.md
```

## How to Run

1.  **Prerequisites:**

    - Ensure you have Python 3.8 or newer installed.

2.  **Clone the repository:**

    ```bash
    git clone [https://github.com/your-username/library-management-system.git](https://github.com/your-username/library-management-system.git)
    ```

3.  **Navigate to the project directory:**

    ```bash
    cd library-management-system
    ```

4.  **Run the application:**
    ```bash
    python main.py
    ```
    The command-line menu will start, populated with initial sample data for easy testing.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
