#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `py_packaging` package."""


import unittest
from click.testing import CliRunner

from py_packaging import py_packaging
from py_packaging import cli


class TestPy_packaging(unittest.TestCase):
    """Tests for `py_packaging` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'py_packaging.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
