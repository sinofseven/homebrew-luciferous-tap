SHELL = /usr/bin/env bash -xeuo pipefail

fmt-python:
	uv run isort src/ tests/
	uv run black src/ tests/

format: \
	fmt-python

test-unit:
	uv run pytest -vv tests/unit

.PHONY: \
	fmt-python \
	format \
	test-unit
