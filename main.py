# implement a guessing game where the computer has a secret number and we are trying to guess it

import random

def guess(x):
    random_number = random.randint(1, x)