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

## Agent Routing (3 agents)

| Role | Agent File | Tier Class | When to Use |
|---|---|---|---|
| module-architect | `.claude/agents/module-architect.md` | architect | Foundation API design, config patterns, backward compatibility |
| implementer | `.claude/agents/implementer.md` | implementer | Settings, logging, model, error implementation |
| reviewer | `.claude/agents/reviewer.md` | reviewer | Stability review, backward compatibility, API safety |

Selection rule: SMA dispatches the appropriate agent based on task type. Module-architect for design tasks, implementer for coding tasks, reviewer for review tasks.
