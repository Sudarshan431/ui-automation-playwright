# UI Automation Framework (Python + Playwright + Pytest)

This project is a **UI test automation framework** built using:

- **Python**
- **Playwright**
- **Pytest**
- **Page Object Model (POM)**

It automates login scenarios for a public demo web app:

> https://the-internet.herokuapp.com/login

The goal is to demonstrate **clean, maintainable UI test automation** using Python and Playwright with Pytest.

---

## 📁 Project Structure

```text
ui-automation-playwright/
├── pages/
│   ├── __init__.py        # Package marker
│   └── login_page.py      # Page Object for the Login page
├── tests/
│   ├── __init__.py        # Package marker
│   └── test_login.py      # UI test cases (positive + negative)
├── requirements.txt       # Python dependencies
├── pytest.ini             # Pytest configuration
├── .gitignore             # Ignore venv, cache, etc.
└── README.md              # Project documentation
