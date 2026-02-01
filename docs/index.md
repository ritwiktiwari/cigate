# cigate

Python-first CI policy gate that validates repository hygiene and tooling standards.

## Installation

Install using pip:

```bash
pip install cigate
```

Or using uv (recommended):

```bash
uv add cigate
```

## Quick Start

```python
import cigate

print(cigate.__version__)
```

### Command Line Interface

cigate provides a command-line interface:

```bash
# Show version
cigate --version

# Say hello
cigate hello World
```

## Development

### Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) for package management

### Setup

Clone the repository and install dependencies:

```bash
git clone https://github.com/ritwiktiwari/cigate.git
cd cigate
uv sync --group dev
```

### Running Tests

```bash
uv run pytest
```

### Code Quality

```bash
# Lint
uv run ruff check .

# Format
uv run ruff format .

# Type check
uv run ty check
```

### Prek Hooks

Install prek hooks:

```bash
prek install
```

## License

This project is licensed under the Apache-2.0 License - see the [LICENSE](https://github.com/ritwiktiwari/cigate/blob/main/LICENSE) file for details.
