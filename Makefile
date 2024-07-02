.PHONY: install lint format check test coverage pr-ready publish

SRC_DIR := ./PTT

# Install dependencies (with dev deps for development)
install:
	@poetry install --with dev

# Run linters
lint:
	@poetry run ruff check $(SRC_DIR)
	@poetry run isort --check-only $(SRC_DIR)

# Format code
sort:
	@poetry run isort $(SRC_DIR)

# Type checking
check:
	@poetry run pyright

# Run tests
test:
	@poetry run pytest
	@poetry run pyright $(SRC_DIR)

# Run tests with coverage
coverage:
	@poetry run pytest --cov=$(SRC_DIR) --cov-report=xml --cov-report=term
	@poetry run pyright $(SRC_DIR)

pr-ready: clean format lint test

publish:
	@poetry publish --build