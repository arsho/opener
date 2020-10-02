# Opener

[![Build Status](https://travis-ci.org/arsho/opener.svg?branch=master)](https://travis-ci.org/arsho/opener)
[![codecov](https://codecov.io/gh/arsho/opener/branch/master/graph/badge.svg)](https://codecov.io/gh/arsho/opener)
![PyPI](https://img.shields.io/pypi/v/opener)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/opener)
![Lines of code](https://img.shields.io/tokei/lines/github/arsho/opener)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/arsho/opener)
![GitHub contributors](https://img.shields.io/github/contributors/arsho/opener)
![PyPI - License](https://img.shields.io/pypi/l/opener)

Opener is a puzzle solver Python package. Currently it solves the *Open the lock* puzzle.
The package can be found in the [Python Package Index (PyPI)](https://pypi.org/project/opener/).

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

### Example 1

![Three Digits Open the Lock Puzzle Example](https://raw.githubusercontent.com/arsho/opener/master/examples/open_the_lock_example_1.png)

The above figure outlines a three digits *Open the Lock* puzzle. A valid unlock key of the above puzzle is: `679`

[example_1.py](https://github.com/arsho/opener/blob/master/examples/example_1.py) shows how to use [opener](https://pypi.org/project/opener/) package to solve the above puzzle.


Solution of the above *Open the lock* puzzle:

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

### Example 2

![Four Digits Open the Lock Puzzle Example](https://raw.githubusercontent.com/arsho/opener/master/examples/open_the_lock_example_2.png)

The above figure outlines another *Open the Lock* puzzle with four digits combination. A valid unlock key of the above puzzle is: `9876`

[example_2.py](https://github.com/arsho/opener/blob/master/examples/example_2.py) shows how to use [opener](https://pypi.org/project/opener/) package to solve the above puzzle.


Solution of the above *Open the lock* puzzle:

```python
from opener import get_keys

number_of_positions = 4
invalid_digits = (5, 1, 2, 4)
similarity_conditions = (
    ([3, 5, 4, 8], 1),
    ([4, 6, 7, 1], 2),
    ([3, 7, 8, 1], 2),
    ([8, 3, 9, 7], 3),
    ([2, 9, 3, 4], 1),
    ([5, 1, 3, 6], 1),
)
invalid_positioned_values = ((3, 8, 2), (5, 7, 3, 9),
                             (4, 8, 9, 3), (8, 1, 7, 4))
valid_positioned_values = ((5,), (1,), (3,), (6,))
unlock_keys = get_keys(number_of_positions,
                       similarity_conditions,
                       invalid_digits,
                       invalid_positioned_values,
                       valid_positioned_values)
for key in unlock_keys:
    print(key)
    # 9876

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

Please read the [development guideline](Development.md) before contribution.

