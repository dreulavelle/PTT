.PHONY: install format sort test coverage pr-ready publish clean

SRC_DIR := ./PTT

# Install dependencies (with dev deps for development)
install:
	@poetry install --with dev

clean:
	@find . -type f -name '*.pyc' -exec rm -f {} +
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type d -name '.pytest_cache' -exec rm -rf {} +
	@find . -type d -name '.ruff_cache' -exec rm -rf {} +

# Run black
format:
	@poetry run black $(SRC_DIR)

# Sort imports
sort:
	@poetry run isort $(SRC_DIR)

# Run tests
test:
	@poetry run pytest

# Run tests with coverage
coverage:
	@poetry run pytest --cov=$(SRC_DIR) --cov-report=xml --cov-report=term

pr-ready: sort format test

publish:
	@poetry publish --build