.PHONY: install lint sort test coverage pr-ready publish

SRC_DIR := ./PTT

# Install dependencies (with dev deps for development)
install:
	@poetry install --with dev

# Run linters
lint:
	@poetry run ruff check $(SRC_DIR)

# Format code
sort:
	@poetry run isort $(SRC_DIR)

# Run tests
test:
	@poetry run pytest

# Run tests with coverage
coverage:
	@poetry run pytest --cov=$(SRC_DIR) --cov-report=xml --cov-report=term

pr-ready: sort lint test

publish:
	@poetry publish --build