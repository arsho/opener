from itertools import permutations


class LockPuzzleSolver(object):
    def __init__(self, number_of_positions, similarity_conditions,
                 invalid_digits=None,
                 invalid_positioned_values=None,
                 valid_positioned_values=None):
        self.number_of_positions = number_of_positions
        self.invalid_digits = invalid_digits
        self.invalid_positioned_values = invalid_positioned_values
        self.valid_positioned_values = valid_positioned_values
        self.domains = self.get_domains()
        self.similarity_conditions = similarity_conditions

    def get_domains(self):
        valid_digits = [i for i in range(10) if i not in self.invalid_digits]
        return list(permutations(valid_digits, self.number_of_positions))

    def validate_similarity(self, sequence, condition):
        matching_sequence, expected_similarity = condition
        d = {}
        e = {}
        count = 0
        for i in sequence:
            d[i] = d.get(i, 0) + 1
        for i in matching_sequence:
            e[i] = e.get(i, 0) + 1
        for i in d:
            if i in e:
                count += min(d[i], e[i])
        return count == expected_similarity

    def get_unlock_keys(self):
        unlock_keys = []
        for ar in self.domains:
            is_valid = True
            for i in range(self.number_of_positions):
                if ar[i] in self.invalid_positioned_values[i]:
                    is_valid = False
                    break
            if is_valid:
                for i in range(self.number_of_positions):
                    if ar[i] in self.valid_positioned_values[i]:
                        for condition in self.similarity_conditions:
                            if not self.validate_similarity(ar, condition):
                                is_valid = False
                                break
                        if is_valid:
                            unlock_keys.append(ar)
                        else:
                            break
        return unlock_keys


if __name__ == "__main__":
    invalid_digits = (5, 2, 3)
    similarity_conditions = (
        ([9, 6, 4], 2),
        ([2, 8, 6], 1),
        ([1, 4, 7], 1),
        ([1, 8, 9], 1)
    )
    invalid_positioned_values = ((9, 1), (6, 8, 4), (4, 6, 7))
    valid_positioned_values = ((1,), (8,), (9,))
    number_of_positions = 3
    solver = LockPuzzleSolver(number_of_positions, similarity_conditions,
                              invalid_digits,
                              invalid_positioned_values,
                              valid_positioned_values)
    for ar in solver.get_unlock_keys():
        print(ar)

    invalid_digits = (7, 3, 8)
    similarity_conditions = (
        ([6, 8, 2], 1),
        ([6, 1, 4], 1),
        ([2, 0, 6], 2),
        ([3, 8, 0], 1)
    )
    invalid_positioned_values = ((6, 2, 3), (1, 0, 8), (4, 6, 0))
    valid_positioned_values = ((6,), (8,), (2,))
    number_of_positions = 3
    solver = LockPuzzleSolver(number_of_positions, similarity_conditions,
                              invalid_digits,
                              invalid_positioned_values,
                              valid_positioned_values)
    for ar in solver.get_unlock_keys():
        print(ar)
