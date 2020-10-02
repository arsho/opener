# Opener

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
 
## Contribute

Contributions are welcome from the community. Questions can be asked on the
[issues page](https://github.com/arsho/opener/issues). Before creating a new issue, please take a moment to search
and make sure a similar issue does not already exist. If one does exist, you
can comment (most simply even with just a `:+1:`) to show your support for that
issue.

If you have direct contributions you would like considered for incorporation
into the project you can [fork this repository](https://github.com/arsho/opener) and
[submit a pull request](https://github.com/arsho/opener/pulls) for review.