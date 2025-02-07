# Testing Showcase

## Overview
This project demonstrates automated testing skills in Python. It includes:
- **Unit Testing** (unittest)
- **Mock Testing** (unittest.mock)
- **API Testing** (Flask test client)
- **Integration Testing** (SQLAlchemy + database)
- **UI Testing** (Selenium)
- **Performance Testing** (pytest-benchmark)

## Installation
```bash
git clone https://github.com/the-world-at-large/testing-showcase.git
cd testing-showcase
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running Tests
Run all tests:
```bash
pytest tests/
```
Run a specific test:
```bash
pytest tests/test_unit.py
```
Run UI tests:
```bash
pytest tests/test_ui.py
```

## Test Descriptions

### Unit Tests (`tests/test_unit.py`)
Validate `add()` and `multiply()` functions, checking different input values and error handling.

### Mock Tests (`tests/test_mock.py`)
Mock `requests.get()` to test API request handling.

### API Tests (`tests/test_api.py`)
Test Flask endpoints `/ping` and `/sum`, ensuring correct API responses.

### Integration Tests (`tests/test_integration.py`)
Verify SQLite database interactions using SQLAlchemy.

### UI Tests (`tests/test_ui.py`)
Use Selenium to check the page title of `example.com`.

### Performance Tests (`tests/test_perf.py`)
Measure `slow_function()` execution time using `pytest-benchmark`.

## Contact
Author - [the-world-at-large](https://github.com/the-world-at-large)
