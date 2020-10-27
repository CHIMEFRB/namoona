#!/usr/bin/env python
# -*- coding: utf-8 -*-

def test_import():
	try:
		import {{cookiecutter.project}}
	except Exception as error:
		raise(error)