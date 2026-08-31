PYTHON ?= python3
.DEFAULT_GOAL := help
.PHONY: help install test tests examples clean

help:
	@$(PYTHON) -c "import re; f=open('Makefile').read(); [print('  {:<24s} {}'.format(*m.groups())) for m in re.finditer(r'^([a-z_-]+):.*?## (.+)', f, re.M)]"

install:
	$(PYTHON) -m pip install -e ".[dev]"

test: tests

tests:
	$(PYTHON) -m pytest --cov-branch --cov=nanotot --cov-report=term-missing --cov-report=html nanotot/tests

examples:
	mkdir -p examples/out
	$(PYTHON) -m nanotot pack --src examples/tiny --out examples/out/clone
	$(PYTHON) -m nanotot child --src examples/tiny --out examples/out/baby
	$(PYTHON) -m nanotot child --src examples/tiny --out examples/out/baby-keep --keep-eye-md

clean:
	rm -rf dist build *.egg-info .pytest_cache .coverage htmlcov examples/out
