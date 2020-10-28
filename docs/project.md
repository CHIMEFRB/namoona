When using the [namoona](https://github.com/chimefrb/namoona) template it will automatically setup
the following components for your backend.

## Project Layout

    <repository>                # Project Root
    ├── <package_name>          # Python Package Root
        ├── analysis/           # Location for low-level analysis code, e.g. functions
        ├── backend/            # Maestro Configuration File + Example API
        ├── pipelines/          # Analysis Pipelines, generally collection of routines.
        ├── routines/           # Analysis routines, generally collection of analysis functions.
        ├── utilities/          # Common code utilities
        docs                    # Technical Documentation
        tests                   # Tests

        .github/workflows       # Continous Integration Config
        .pre-commit-config.yml  # Configuration for pre-commit
        .gitignore              # Git configuration

        pyproject.toml          # The python package management
        poetry.lock             # Lock file for python packages
        mkdocs.yml              # Configuration for generating docs
        LICENCE                 # Project Licence
        README.md               # README for the project

## Project Components
When setting up a project with `namoona` the following components come pre-configured:

  - *Project Layout* with ideal module setup
  - *Backend Configuration* file for `maestro`
  - *Continous Integration* setup via Github Actions
  - *Pre-Commit* configuration hooks for:
    - Code Formatting
    - Documentation Style
    - Python Type Hinting
    - Checks for `yaml`, `json` & `toml` files
  - *Documentation* setup via [mkdocs-material](https://squidfunk.github.io/mkdocs-material/getting-started/)
  - *Testing* setup through [pytest](https://docs.pytest.org/en/stable/)


