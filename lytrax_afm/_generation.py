from math import isnan
from ._utils import get_random_int


def generate_afm(
    force_first_digit: int = None,
    pre99: bool = False,
    individual: bool = False,
    legal_entity: bool = False,
    repeat_tolerance: int = None,
    valid: bool = True
) -> str:
    min = 7 if legal_entity else 1
    max = 4 if individual else 9
    repeat_of = None if not repeat_tolerance and repeat_tolerance != 0 else repeat_tolerance
    digit = force_first_digit if force_first_digit is not None and not isnan(force_first_digit) \
                              else (0 if pre99 else get_random_int(min, max))
    last_gen_digit = digit
    repeats = 0
    body = str(digit)
    sum = digit * 0x100

    for i in range(7, 0, -1):
        digit = get_random_int(0, 9, last_gen_digit if repeat_of is not None and repeats >= repeat_of else None)
        body += str(digit)
        sum += digit << i
        if digit == last_gen_digit:
            repeats += 1
        else:
            repeats = 0
        last_gen_digit = digit
    
    validator = sum % 11
    d9_valid = 0 if validator >= 10 else validator
    d9 = d9_valid if valid else get_random_int(0, 9, d9_valid)

    return body + str(d9)

def generate_valid_afm(**args) -> str:
    args['valid'] = True
    return generate_afm(**args)

def generate_invalid_afm(**args) -> str:
    args['valid'] = False
    return generate_afm(**args)
