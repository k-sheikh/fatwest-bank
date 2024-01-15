## FatWest Bank Application

---

### Description

FatWest Bank Application is a sophisticated, console-based banking system implemented in Python. It offers an interactive experience for users to manage their banking needs, including account creation, deposits, withdrawals, and user information management in a secure environment, now featuring hashed password storage for enhanced security.

### Features

- **User Registration and Login**: Secure system for user authentication with password hashing for added security.
- **Account Management**: Users can create and manage multiple types of accounts (e.g., Savings, Current).
- **Deposits and Withdrawals**: Facilitates basic banking transactions.
- **Transaction Validation**: Ensures the integrity and security of transactions.
- **Database Integration**: Utilises a database for persistent data storage and retrieval.
- **Modular Code Structure**: Codebase is organised into distinct modules:
  - `main`: Main application entry point.
  - `user`: Manages user data and authentication.
  - `account`: Handles account-related operations.
  - `bank`: Oversees overall banking functionalities.
  - `utilities`: Contains utility functions for common tasks.
  - `database`: Manages database interactions.

### Installation

#### Prerequisites

- Python 3.6 or higher.
- bcrypt library (for password hashing)

#### Setup

Clone the repository:

```
git clone https://github.com/k-sheikh/fatwest-bank
```

Install the required Python package:

```
pip install bcrypt
```

### Usage

Run the application using Python:

```
python main.py
```

Follow the on-screen prompts to navigate through the application.

### Future Enhancements

- **Enhanced Security Measures**: Further improve security protocols, including two-factor authentication.
- **User Interface Improvement**: Develop a more sophisticated user interface.
- **Extended Banking Features**: Incorporate features like account statements, online transfers, and loan services.
- **Scalability**: Refine the application for scalability and efficiency in handling a larger user base.

### Acknowledgments

- This project is an ongoing development effort as part of a learning exercise in advanced software development and modular programming.
