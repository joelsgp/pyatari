# template-python-base
Base for python templates.

To find all my templates, go to:
- https://github.com/joelsgp?tab=repositories&q=&type=template

Includes:
- `README.md`
    - that's this file
    - https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
    - https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
- `template_package/`
    - `__init__.py`
        - `__version__`
        - https://packaging.python.org/en/latest/guides/single-sourcing-package-version/
        - https://peps.python.org/pep-0396/
    - `__main__.py`
        - https://docs.python.org/3/library/__main__.html
    - https://docs.python.org/3/tutorial/modules.html
- `.gitignore`
    - https://github.com/github/gitignore/blob/main/Python.gitignore
    - https://git-scm.com/docs/gitignore
- `LICENSE`
    - https://www.gnu.org/licenses/gpl-3.0.en.html
    - https://choosealicense.com/licenses/gpl-3.0/
    - https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository
- `Pipfile`
    - includes dev dependencies
        - build
            - https://pypa-build.readthedocs.io/en/stable/
            - https://pypi.org/project/build/
            - https://github.com/pypa/build
        - black
            - https://black.readthedocs.io/en/stable/
            - https://pypi.org/project/black/
            - https://github.com/psf/black
        - isort
            - https://pycqa.github.io/isort/
            - https://pypi.org/project/isort/
            - https://github.com/pycqa/isort/
    - https://pipenv.pypa.io/en/latest/
    - https://pypi.org/project/pipenv/
    - https://github.com/pypa/pipenv
- `pyproject.toml`
    - https://peps.python.org/pep-0621/
    - https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html
    - https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/
    - https://pycqa.github.io/isort/docs/configuration/config_files.html#pyprojecttoml-preferred-format
