.PHONY: install run test lint format typecheck quality check clean

install: .venv ## Crée le venv et installe les dépendances

.venv: pyproject.toml poetry.lock
	poetry install
	touch .venv

run: .venv ## Lance l'application
	poetry run python app/main.py

test: .venv ## Lance les tests
	poetry run pytest

lint: .venv ## Vérifie le style et les erreurs avec ruff
	poetry run ruff check .
	poetry run ruff format --check .

format: .venv ## Corrige et formate le code avec ruff
	poetry run ruff check --fix .
	poetry run ruff format .

typecheck: .venv ## Vérifie les types avec mypy
	poetry run mypy app tests

quality: format lint typecheck ## Formate, lint et vérifie les types

check: lint typecheck test ## Lance lint, typecheck et tests

clean: ## Supprime le venv et les caches
	rm -rf .venv .pytest_cache .ruff_cache .mypy_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
