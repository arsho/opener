from itertools import permutations


class OpenTheLockPuzzleSolver(object):
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
                            unlock_keys.append("".join([str(i) for i in ar]))
                        else:
                            break
        return unlock_keys


def get_keys(number_of_positions,
             similarity_conditions,
             invalid_digits,
             invalid_positioned_values,
             valid_positioned_values):
    solver = OpenTheLockPuzzleSolver(number_of_positions,
                                     similarity_conditions,
                                     invalid_digits,
                                     invalid_positioned_values,
                                     valid_positioned_values)
    return solver.get_unlock_keys()
