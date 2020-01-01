from random import randint

def get_random_int(min, max, not_equal = None):
    result = None

    while True:
        result = randint(min, max)
        if not_equal == None or result != not_equal:
            break

    return result
