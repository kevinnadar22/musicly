# Tests

This directory contains comprehensive tests for the musicly terminal music player.

## Test Structure

- `test_utils.py` - Tests for utility functions in the `player.utils` module
  - URL helpers (parsing URLs, downloading files)
  - File operations (searching, unzipping, cleanup)
  - FFmpeg management (download, detection, configuration)
  - Audio download functionality

## Running Tests

### Install test dependencies

```bash
# Using uv (recommended)
uv pip install --group test

# Or using pip
pip install pytest pytest-cov
```

### Run all tests

```bash
pytest
```

### Run with coverage report

```bash
pytest --cov=player --cov-report=html
```

The coverage report will be generated in the `htmlcov/` directory.

### Run specific test file

```bash
pytest tests/test_utils.py
```

### Run specific test class

```bash
pytest tests/test_utils.py::TestUrlHelpers
```

### Run specific test

```bash
pytest tests/test_utils.py::TestUrlHelpers::test_get_path_from_url_valid
```

### Run with verbose output

```bash
pytest -v
```

## Test Coverage

The tests use `unittest.mock` for mocking external dependencies like:
- File system operations
- Network requests
- Subprocess calls
- System commands

This ensures tests run quickly and don't require external resources.

## Writing New Tests

When adding new tests:

1. Follow the existing structure with test classes
2. Use descriptive test names that explain what's being tested
3. Mock external dependencies to keep tests isolated
4. Clean up any temporary files created during tests
5. Test both success and failure scenarios
