from random import randint

def get_random_int(min: int, max: int, notEqual = None) -> int:
    result: int

    while True:
        result = randint(min, max)
        if notEqual == None or result != notEqual:
            break

    return result
