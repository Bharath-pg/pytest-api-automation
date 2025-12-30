# 🧪 API Automation Framework — Python + PyTest

A robust API automation framework built using **Python**, **Requests**, and **PyTest** designed for scalable, maintainable testing of REST APIs.

---

## 🚀 Overview

This project demonstrates a modular API testing framework that includes:
- API client utilities (`utils/api_client.py`)
- Structured tests with PyTest and fixtures
- Logging and HTML reporting
- JSON Schema / Contract validation
- Parametrized
- Clean folder structure for real-world usage

---

## 🧠 What This Framework Covers

| Feature | Status |
|---------|--------|
| GET / POST API tests | ✅ |
| Auth headers + fixtures | ✅ |
| PyTest + HTML reporting | ✅ |
| JSON Schema validation | ✅ |
| Parametrized tests | ✅ |

## 📂 Project Structure

```
api-automation-pytest/
├── config/
│   └── config.py                  # Base URL, token, constants
│
├── schema/
│   └── user_schema.py             # JSON schema for contract validation
│
├── utils/
│   ├── api_client.py              # GET/POST wrapper + timeout/retry support
│   ├── logger.py                  # Centralized logger for test runs
│   └── validators.py              # JSON schema + soft assertion validator
│
├── tests/
│   └── test_users.py              # Parametrized, schema, retry tests
│
├── reports/                       # (Generated) HTML execution reports
│
├── conftest.py                    # Fixtures: auth headers & setup/teardown
├── pytest.ini                     # Pytest configuration (logging, reports)
├── requirements.txt               # Dependencies list (requests, pytest, etc.)
├── .gitignore                     # Ignore pycache, venv, logs, reports, etc.
└── README.md                      # Project documentation
```
