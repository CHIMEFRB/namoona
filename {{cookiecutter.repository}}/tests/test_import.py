#!/usr/bin/env python
"""Generic tests for frb-datatrails."""
import {{project}}


def test_project_import():
    """Simple check to test for package importability."""
    assert isinstance({{project}}.__file__, str)


def test_analysis_function():
    """Check if the seed function works."""
    flavor = "str"
    uuid = {{project}}.analysis.seed.get_uuid(flavor=flavor)
    assert isinstance(uuid, str)
