.PHONY: help install clean format sort test debug coverage pr-ready publish

SRC_DIR := ./PTT

help:
	@echo "Usage: make <target>"
	@echo "Available targets:"
	@echo "  install     Install dependencies"
	@echo "  clean       Clean up temporary files"
	@echo "  format      Format code"
	@echo "  sort        Sort imports"
	@echo "  test        Run tests"
	@echo "  debug       Debug tests"
	@echo "  coverage    Generate coverage report"
	@echo "  pr-ready    Run format, sort, and test"
	@echo "  publish     Publish to PyPI"

install:
	@uv sync --all-extras

clean:
	@find . -type f -name '*.pyc' -exec rm -f {} +
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type d -name '.pytest_cache' -exec rm -rf {} +
	@find . -type d -name '.ruff_cache' -exec rm -rf {} +

keywords:
	@uv run python cli.py combine ./PTT/keywords/

format:
	@uv run black $(SRC_DIR)

sort:
	@uv run isort $(SRC_DIR)
	@uv run python cli.py dedupe ./PTT/keywords/combined-keywords.txt

lint:
	@uv run ruff check $(SRC_DIR)

test: clean
	@uv run pytest -n 4 --dist=loadscope tests

diff:
	@git diff HEAD~1 HEAD

debug:
	@uv run pytest tests/test_main.py::test_debug_releases_parse -v -ss

coverage: clean
	@uv run pytest -n 4 --dist=loadscope tests --cov=$(SRC_DIR) --cov-report=xml --cov-report=term

pr-ready: sort format test

publish:
	@uv build
	@uv publish