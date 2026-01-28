"""cigate CLI - validate repository hygiene and tooling standards."""

from __future__ import annotations

from enum import Enum
from typing import Optional

import typer

from cigate import __version__


class Profile(str, Enum):
    """Policy profile strictness level."""

    starter = "starter"
    team = "team"
    strict = "strict"


class OutputFormat(str, Enum):
    """Output format for check results."""

    text = "text"
    json = "json"


class TypecheckerChoice(str, Enum):
    """Which type checker to configure."""

    auto = "auto"
    mypy = "mypy"
    pyright = "pyright"


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"cigate {__version__}")
        raise typer.Exit()


app = typer.Typer(
    name="cigate",
    help="Python-first CI policy gate. Validates repository hygiene and tooling standards.",
    no_args_is_help=True,
    rich_markup_mode="rich",
)


@app.command()
def check(
    profile: Profile = typer.Option(
        Profile.starter,
        "--profile",
        "-p",
        help="Policy profile to validate against.",
        case_sensitive=False,
    ),
    output_format: OutputFormat = typer.Option(
        OutputFormat.text,
        "--format",
        "-f",
        help="Output format for results.",
        case_sensitive=False,
    ),
    run: bool = typer.Option(
        False,
        "--run",
        help="Execute tools (mypy, ruff, etc.) instead of only checking configuration.",
    ),
    root: Optional[str] = typer.Option(
        None,
        "--root",
        "-r",
        help="Project root directory. Defaults to current working directory.",
    ),
) -> None:
    """Validate the current project against cigate policies.

    Checks repository configuration, tooling setup, and optionally runs
    the configured tools to verify they pass.

    Exit codes: 0 = pass, 1 = policy violations found, 2 = tool/config error.
    """
    typer.echo(
        f"[stub] cigate check: profile={profile.value}, "
        f"format={output_format.value}, run={run}, root={root}"
    )


@app.command()
def fix(
    typechecker: TypecheckerChoice = typer.Option(
        TypecheckerChoice.auto,
        "--typechecker",
        "-t",
        help="Type checker to configure. 'auto' detects from existing config.",
        case_sensitive=False,
    ),
    yes: bool = typer.Option(
        False,
        "--yes",
        "-y",
        help="Skip confirmation prompts and apply all fixes.",
    ),
    root: Optional[str] = typer.Option(
        None,
        "--root",
        "-r",
        help="Project root directory. Defaults to current working directory.",
    ),
) -> None:
    """Auto-fix missing or misconfigured tooling in the current project.

    Generates or updates configuration for type checkers, linters, and CI
    pipelines to satisfy the selected cigate profile.
    """
    typer.echo(
        f"[stub] cigate fix: typechecker={typechecker.value}, "
        f"yes={yes}, root={root}"
    )


@app.callback()
def main(
    version: bool = typer.Option(
        False,
        "--version",
        "-V",
        help="Show cigate version and exit.",
        callback=_version_callback,
        is_eager=True,
    ),
) -> None:
    """cigate - Python-first CI policy gate."""
