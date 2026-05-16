SHELL = /usr/bin/env bash -xeuo pipefail

fmt-python:
	@uv run isort src/ tests/
	@uv run black src/ tests/

format: \
	fmt-python

test-unit:
	@uv run pytest -vv tests/unit

create-formula-by-publishing-release:
	@PYTHONPATH=src \
		uv run src/handlers/create_formula_by_published_release/index.py

.PHONY: \
	fmt-python \
	format \
	test-unit \
	create-formula-by-publishing-release
