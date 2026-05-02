# ember-shared

## What this package does

Stable foundation package for the Ember Bio platform. Provides configuration
management (Pydantic BaseSettings), structured JSON logging, base model classes,
and shared exception types used by all other Python repos.

## Key modules

- `settings.py` — Pydantic BaseSettings for app configuration
- `logging.py` — Structured JSON logging setup
- `models.py` — Common base Pydantic models
- `errors.py` — Shared exception hierarchy

## How to run tests

```bash
uv sync --extra dev
uv run pytest --cov
```

## Conventions

- All models inherit from Pydantic BaseModel
- Use structured logging (JSON) — never print()
- This package has zero internal Ember dependencies
- Changes here affect all downstream repos — keep the API stable
- Lint with ruff: `uv run ruff check src/ tests/`
