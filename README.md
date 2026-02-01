# cigate

[![CI](https://github.com/ritwiktiwari/cigate/actions/workflows/ci.yml/badge.svg)](https://github.com/ritwiktiwari/cigate/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/cigate.svg)](https://badge.fury.io/py/cigate)
[![codecov](https://codecov.io/gh/ritwiktiwari/cigate/branch/main/graph/badge.svg)](https://codecov.io/gh/ritwiktiwari/cigate)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![ty](https://img.shields.io/badge/type--checked-ty-blue?labelColor=orange)](https://github.com/astral-sh/ty)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-yellow.svg)](https://github.com/ritwiktiwari/cigate/blob/main/LICENSE)


**Python-first CI policy gate** -- validates repository hygiene and tooling
standards before code reaches your CI pipeline.

---

## What is cigate?

cigate is an opinionated CLI tool that checks whether your Python project
follows modern development practices: type checking is configured, linters
are set up, dependency lockfiles exist, tests are present, and CI pipelines
meet minimum standards.

It does **not** replace your linter, type checker, or security scanner.
Instead, it answers the question: _"Is this repo even set up to run those
tools correctly?"_

One command. Clear results. Actionable fixes.

## How is it different?

| Tool | What it does | What cigate does differently |
|------|-------------|------------------------------|
| **ruff / pylint** | Lint your code | cigate checks that a linter is *configured* |
| **mypy / pyright** | Type-check your code | cigate checks that a type checker is *present and configured* |
| **pre-commit** | Run hooks on commit | cigate validates the full CI policy, not just git hooks |
| **cookiecutter** | Scaffold new projects | cigate audits *existing* projects continuously |

cigate sits one level above individual tools. It is the gate that asks:
_"Does this repository meet our team's baseline standards?"_

## Quick start

```bash
# Install with uv
uv tool install cigate

# Or install with pip
pip install cigate

# Check the current project
cigate check

# Check with a stricter profile
cigate check --profile strict

# Auto-fix missing configuration
cigate fix
```

## Commands

### `cigate check`

Validate the current project against a policy profile.

```
Options:
  -p, --profile   Policy profile: starter, team, strict  [default: starter]
  -f, --format    Output format: text, json               [default: text]
      --run       Execute tools, not just check config     [default: off]
  -r, --root      Project root directory                   [default: cwd]
```

Exit codes:
- **0** -- all checks pass
- **1** -- policy violations found
- **2** -- configuration or tool error

### `cigate fix`

Auto-generate or repair tooling configuration.

```
Options:
  -t, --typechecker  Type checker: auto, mypy, pyright  [default: auto]
  -y, --yes          Skip confirmation prompts           [default: off]
  -r, --root         Project root directory              [default: cwd]
```

## What does cigate check? (v1 roadmap)

- **pyproject.toml** -- exists, well-formed, has required metadata
- **Type checker** -- mypy or pyright is configured and (optionally) passes
- **Linter** -- ruff or pylint is configured
- **Tests** -- test directory exists, pytest is configured
- **Lockfile** -- `uv.lock`, `poetry.lock`, or equivalent is present
- **CI** -- GitHub Actions workflow exists with lint/test/type-check steps
- **Docs** -- README exists and is non-empty
- **Security** -- no secrets in tracked files (basic pattern checks)

## Project status

**v0.0.1** -- scaffold only. Commands are defined but do not perform real
checks yet. See the roadmap for planned features.

## License

Apache 2.0 -- see [LICENSE](LICENSE).
