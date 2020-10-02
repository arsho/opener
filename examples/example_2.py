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
