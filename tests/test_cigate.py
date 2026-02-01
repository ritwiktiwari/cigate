"""Tests for cigate."""

from typer.testing import CliRunner

from cigate import __version__
from cigate.cli.main import app

runner = CliRunner()


def test_version() -> None:
    """Test that version is defined."""
    assert __version__ is not None
    assert isinstance(__version__, str)


def test_cli_version() -> None:
    """Test CLI version command."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.stdout


def test_cli_check_default() -> None:
    """Test CLI check command with defaults."""
    result = runner.invoke(app, ["check"])
    assert result.exit_code == 0
    assert "cigate check" in result.stdout


def test_cli_check_with_profile() -> None:
    """Test CLI check command with a profile option."""
    result = runner.invoke(app, ["check", "--profile", "strict"])
    assert result.exit_code == 0
    assert "profile=strict" in result.stdout


def test_cli_fix_default() -> None:
    """Test CLI fix command with defaults."""
    result = runner.invoke(app, ["fix"])
    assert result.exit_code == 0
    assert "cigate fix" in result.stdout


def test_cli_fix_with_typechecker() -> None:
    """Test CLI fix command with typechecker option."""
    result = runner.invoke(app, ["fix", "--typechecker", "mypy"])
    assert result.exit_code == 0
    assert "typechecker=mypy" in result.stdout
