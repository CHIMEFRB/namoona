#!/usr/bin/env python
# -*- coding: utf-8 -*-

def test_project_import():
	try:
		import {{cookiecutter.project}}
	except Exception as error:
		raise(error)

def test_analysis_function():
	from {{cookiecutter.project}}.analysis import seed
	flavor = "str"
	uuid = seed.get_uuid(flavor=flavor)
	assert isinstance(uuid, str)