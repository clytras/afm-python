import re


def validate_afm(afm: str, extended_result: bool = False):
    if len(afm) != 9:
        return {
            'valid': False,
            'error': "length"
        } if extended_result else False

    if not re.match(r"^\d+$", afm):
        return {
            'valid': False,
            'error': "nan"
        } if extended_result else False

    if afm == "0" * 9:
        return {
            'valid': False,
            'error': "zero"
        } if extended_result else False

    body = afm[:8]
    sum = 0
    
    for i in range(len(body)):
        digit = body[i]
        sum += int(digit) << (8 - i)
    
    calc = sum % 11;
    d9 = int(afm[8])
    valid = calc % 10 == d9

    if extended_result:
        return {
            'valid': valid
        } if valid else {
            'valid': valid,
            'error': 'invalid'
        }
    
    return valid
