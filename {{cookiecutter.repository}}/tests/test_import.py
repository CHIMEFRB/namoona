#!/usr/bin/env python
"""Generic tests for frb-datatrails."""
import datatrail


def test_project_import():
    """Simple check to test for package importability."""
    assert isinstance(datatrail.__file__, str)


def test_analysis_function():
    """Check if the seed function works."""
    flavor = "str"
    uuid = datatrail.analysis.seed.get_uuid(flavor=flavor)
    assert isinstance(uuid, str)
