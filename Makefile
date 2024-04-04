# create makefile for the project

.PHONY: test

# Run pytests on tests dir
test:
	@poetry run pytest tests -s -vv