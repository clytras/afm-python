__author__ = 'lytrax'

from ._validation import validate_afm as validate_afm
from ._generation import \
    generate_afm as generate_afm, \
    generate_valid_afm as generate_valid_afm, \
    generate_invalid_afm as generate_invalid_afm

__all__ = ['validate_afm', 'generate_afm', 'generate_valid_afm', 'generate_invalid_afm']
