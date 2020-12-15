# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
import string
import random

class Game:
    """Form a complex number."""
    def __init__(self):
        """Form a complex number."""
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))
    def is_valid(self,word):
        """Form a complex number."""
        if len(word) <= 0:
            return False
        for i in word:
            test = i in self.grid
        return test
