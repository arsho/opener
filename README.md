# Opener

[![Build Status](https://travis-ci.org/arsho/opener.svg?branch=master)](https://travis-ci.org/arsho/opener)
![PyPI](https://img.shields.io/pypi/v/opener)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/opener)
[![codecov](https://codecov.io/gh/arsho/opener/branch/master/graph/badge.svg)](https://codecov.io/gh/arsho/opener)
![Lines of code](https://img.shields.io/tokei/lines/github/arsho/opener)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/arsho/opener)
![GitHub contributors](https://img.shields.io/github/contributors/arsho/opener)
![PyPI - Downloads](https://img.shields.io/pypi/dm/opener)
![PyPI - License](https://img.shields.io/pypi/l/opener)

Opener is a puzzle solver Python package. Currently it solves the *Open the lock* puzzle.

This package can be used on Linux/Unix, Mac OS and Windows systems.

## Features

- Get keys for *Open the lock* puzzle.

## Installation

You can install the *opener* from [PyPI](https://pypi.org/project/opener/):

```bash
pip install opener
```

The *opener* is supported on Python 2.7, as well as Python 3.4 and above.

## How to use

![Puzzle Example](https://raw.githubusercontent.com/arsho/opener/master/resources/open_the_lock.png)

The above figure outlines an *Open the Lock* puzzle. A valid unlock key of the above puzzle is: `679`

[example.py](example.py) shows how to use [opener](https://pypi.org/project/opener/) package to solve the above puzzle.


To solve an *Open the lock* puzzle:

```python
from opener import get_keys

number_of_positions = 3
invalid_digits = (5, 2, 3)
similarity_conditions = (
    ([9, 6, 4], 2),
    ([2, 8, 6], 1),
    ([1, 4, 7], 1),
    ([1, 8, 9], 1)
)
invalid_positioned_values = ((9, 1), (6, 8, 4), (4, 6, 7))
valid_positioned_values = ((1,), (8,), (9,))
unlock_keys = get_keys(number_of_positions,
                       similarity_conditions,
                       invalid_digits,
                       invalid_positioned_values,
                       valid_positioned_values)
for key in unlock_keys:
    print(key)
    # 679
 ```

## Authors
- Maintainer: [Ahmedur Rahman Shovon](https://arshovon.com/)
- Please see the [list of contributors](https://github.com/arsho/opener/graphs/contributors) to find the contributors of this project.


 
## Contribute

Contributions are welcome from the community. Questions can be asked on the
[issues page](https://github.com/arsho/opener/issues). Before creating a new issue, please take a moment to search
and make sure a similar issue does not already exist. If one does exist, you
can comment (most simply even with just a `:+1:`) to show your support for that
issue.

If you have direct contributions you would like considered for incorporation
into the project you can [fork this repository](https://github.com/arsho/opener) and
[submit a pull request](https://github.com/arsho/opener/pulls) for review.

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
    pip install -i https://test.pypi.org/simple/ PACKAGE_NAME==PACKAGE_VERSION
    ```
- To upload newer version to TestPyPI, change `version` in `setup.py` and other places where version information is stored. Then create the wheel and upload the files to TestPyPI:
    ```
    python setup.py sdist bdist_wheel
    twine upload --skip-existing --repository testpypi dist/*
    ```
- If there is no error, then the package will be uploaded to TestPyPI.
- To test the TestPyPI package, create a virtual environment, activate it and finally install the package:
    ```
    pip install -i https://test.pypi.org/simple/ PACKAGE_NAME==PACKAGE_VERSION
    ```
- Upload to PyPI. A PyPI account is needed for this which can be registered from [https://pypi.org/](https://pypi.org/):
    ```
    twine upload dist/*
    ```
- If there is no error, then the package will be uploaded to TestPyPI.
- To test the PyPI package, create a virtual environment, activate it and finally install the package:
    ```
    pip install PACKAGE_NAME
    ```
- To upload newer version to PyPI, change `version` in `setup.py` and other places where version information is stored. Then create the wheel and upload the files to PyPI:
    ```
    python setup.py sdist bdist_wheel
    twine upload --skip-existing dist/*
    ```