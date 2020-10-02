## Development Guideline

The following steps can be used to create release package for PyPi.
- Create a virtual environment:
    ```
    python3 -m venv venv
    ```
- Activate virtual environment:
    ```
    source venv/bin/activate
    ```
- Install necessary packages:
    ```
    pip install -r development.txt
    ```
- Run unit tests:
    ```
    python tests/unit_tests.py
    ```
- Run Python linter:
    ```
    pylint opener
    flake8 opener
    ```
- Generate dist files:
    ```
    python setup.py sdist bdist_wheel
    ```
- Upload to TestPyPI which is a separate instance of the Python Package Index. A TestPyPI account is needed for this which can be registered from [https://test.pypi.org/](https://test.pypi.org/):
    ```
    twine upload --repository testpypi dist/*
    ```
- If there is no error, then the package will be uploaded to TestPyPI.
- To test the TestPyPI package, create a virtual environment, activate it and finally install the package:
    ```
    pip install -i https://test.pypi.org/simple/ opener==PACKAGE_VERSION
    ```
- To upload newer version to TestPyPI, change `version` in `setup.py` and other places where version information is stored. Then create the wheel and upload the files to TestPyPI:
    ```
    python setup.py sdist bdist_wheel
    twine upload --skip-existing --repository testpypi dist/*
    ```
- If there is no error, then the package will be uploaded to TestPyPI.
- To test the TestPyPI package, create a virtual environment, activate it and finally install the package:
    ```
    pip install -i https://test.pypi.org/simple/ opener==PACKAGE_VERSION
    ```
- Upload to PyPI. A PyPI account is needed for this which can be registered from [https://pypi.org/](https://pypi.org/):
    ```
    twine upload dist/*
    ```
- If there is no error, then the package will be uploaded to TestPyPI.
- To test the PyPI package, create a virtual environment, activate it and finally install the package:
    ```
    pip install opener
    ```
- To upload newer version to PyPI, change `version` in `setup.py` and other places where version information is stored. Then create the wheel and upload the files to PyPI:
    ```
    python setup.py sdist bdist_wheel
    twine upload --skip-existing dist/*
    ```