"""
opener
======
Open the lock puzzle solver.

Usage
-----
Solve an open the lock puzzle::

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



"""

__version__ = '0.0.2'

from .open_the_lock import get_keys
