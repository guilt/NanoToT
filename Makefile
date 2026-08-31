PYTHON ?= python3
.DEFAULT_GOAL := help
.PHONY: help install test tests unit-tests coverage examples clean format lint

help: ## Show this help
	@$(PYTHON) -c "import re; f=open('Makefile').read(); [print('  {:<24s} {}'.format(*m.groups())) for m in re.finditer(r'^([a-z_-]+):.*?## (.+)', f, re.M)]"

install: ## Editable install with dev extras
	$(PYTHON) -m pip install -e ".[dev]"

test: tests

tests: ## Pytest with branch coverage
	PYTHONPATH=. $(PYTHON) -m pytest --cov-branch --cov=nanotot --cov-report=term-missing --cov-report=html nanotot/tests

unit-tests: tests ## Alias

coverage: tests ## Alias

examples: ## Pack, child, inspect the example organism
	mkdir -p examples/out
	PYTHONPATH=. $(PYTHON) -m nanotot pack --src examples/tiny --out examples/out/clone
	PYTHONPATH=. $(PYTHON) -m nanotot child --src examples/tiny --out examples/out/baby
	PYTHONPATH=. $(PYTHON) -m nanotot child --src examples/tiny --out examples/out/baby-keep --keep-eye-md --keep-ear-md
	PYTHONPATH=. $(PYTHON) -m nanotot inspect --src examples/tiny
	PYTHONPATH=. $(PYTHON) examples/inspect_tree.py

format:
	-$(PYTHON) -m ruff format nanotot examples

lint: format
	-$(PYTHON) -m ruff check nanotot

clean:
	rm -rf dist build *.egg-info .pytest_cache .coverage htmlcov examples/out
