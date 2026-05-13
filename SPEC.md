# toolkit

A Python utility library providing common helpers for development.

## Architecture

Flat module layout — each `.py` in `toolkit/` is a self-contained provider:

| Module | Purpose |
|---|---|
| `async_logger` | Async non-blocking logging via QueueHandler/QueueListener |
| `conman` | Connection manager |
| `currency` | Currency helpers |
| `datastruct` | Data structure utilities |
| `display` | Display/print helpers |
| `fileutils` | File operations |
| `kokoo` | General helpers |
| `logger` | Simple synchronous logger |
| `msexcel` | MS Excel operations |
| `ohlcv` | OHLCV data helpers |
| `optionchain` | Option chain data |
| `redis_client` | Redis client wrapper |
| `scripts` | Script runner helpers |
| `symbols` | Symbol/ticker utilities |
| `telegram` | Telegram bot integration |
| `utilities` | Miscellaneous utilities |
| `webdriver` | Selenium webdriver manager |

## Dependencies

Python 3.10+. Managed via `pyproject.toml` (build-system: setuptools).

## Key Files

- `pyproject.toml` — build config
- `setup.py` — legacy package metadata (to be migrated to pyproject.toml)

## Known Issues

- `setup.py` still uses `distutils.core` (deprecated); should migrate fully to `pyproject.toml`
- `requirements.txt` exists alongside `pyproject.toml` — should consolidate
- No `__init__.py` in `toolkit/` package
