from random import randint

def get_random_int(min: int, max: int, not_equal = None) -> int:
    result: int

    while True:
        result = randint(min, max)
        if not_equal == None or result != not_equal:
            break

    return result
