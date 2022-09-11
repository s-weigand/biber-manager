#!/usr/bin/env python

"""Tests for `biber` package."""

import re

# from biber import biber
from biber_manager import cli
from typer.testing import CliRunner


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.app)
    assert result.exit_code == 0
    assert "biber_manager.cli.main" in result.output
    help_result = runner.invoke(cli.app, ["--help"])
    assert help_result.exit_code == 0
    assert re.search(r"--help\s+Show this message and exit\.", help_result.output)
