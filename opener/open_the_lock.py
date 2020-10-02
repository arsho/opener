"""This script contains the Open the lock solver class.

Additionally, it contains the get_keys function which creates an object
of the solver class using the passed parameters and returns the valid keys.
"""

from itertools import permutations


class OpenTheLockPuzzleSolver:
    """Open the Lock solver class."""

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
        """Returns list of permutations of digits of fixed length"""
        valid_digits = [i for i in range(10) if i not in self.invalid_digits]
        return list(permutations(valid_digits, self.number_of_positions))

    @staticmethod
    def validate_similarity(sequence, condition):
        """Returns a boolean result if the given sequence and
        matching sequence contains a fixed similarity score"""
        matching_sequence, expected_similarity = condition
        occurrences = {}
        matching_occurrences = {}
        count = 0
        for i in sequence:
            occurrences[i] = occurrences.get(i, 0) + 1
        for i in matching_sequence:
            matching_occurrences[i] = matching_occurrences.get(i, 0) + 1
        for i in occurrences:
            if i in matching_occurrences:
                count += min(occurrences[i], matching_occurrences[i])
        return count == expected_similarity

    def get_unlock_keys(self):
        """Returns list of valid unlock keys for the lock."""
        unlock_keys = []
        for domain in self.domains:
            is_valid = True
            for i in range(self.number_of_positions):
                if domain[i] in self.invalid_positioned_values[i]:
                    is_valid = False
                    break
            if not is_valid:
                continue
            for i in range(self.number_of_positions):
                if domain[i] in self.valid_positioned_values[i]:
                    for condition in self.similarity_conditions:
                        if not self.validate_similarity(domain, condition):
                            is_valid = False
                            break
                    if is_valid:
                        unlock_keys.append("".join([str(i) for i in domain]))
                    else:
                        break
        return unlock_keys


def get_keys(number_of_positions,
             similarity_conditions,
             invalid_digits,
             invalid_positioned_values,
             valid_positioned_values):
    """Creates an object of the solver class and
    returns a list of valid keys"""
    solver = OpenTheLockPuzzleSolver(number_of_positions,
                                     similarity_conditions,
                                     invalid_digits,
                                     invalid_positioned_values,
                                     valid_positioned_values)
    return solver.get_unlock_keys()
