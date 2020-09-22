When using the [namoona](https://github.com/chimefrb/namoona) template it will automatically setup
the following components for your backend.

## Project Layout

    <repository>                # Project Root
    ├── <backend>          	    # Python Package Root
        ├── backend/	  		# Maestro Configuration File + Example API
        ├── src/          		# Location for source code
        docs			  		# Technical Documentation
        tests					# Tests

        .github/workflows 		# Continous Integration Config
        .pre-commit-config.yml  # Configuration for pre-commit
        .gitignore              # Git configuration

        pyproject.toml    		# The python package management
        poetry.lock 			# Lock file for python packages
        mkdocs.yml              # Configuration for generating docs
        LICENCE					# Project Licence
        README.md 				# This file

## Project Components
When setting up a project with `namoona` the following components come pre-configured:

  - *Backend Configuration* file for `maestro`
  - *Continous Integration* setup via Github Actions
  - *Pre-Commit Configuration* file
  - *Documentation* setup via mkdocs
  - *Testing* setup through pytest

