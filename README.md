# Greek TIN/AFM Validator and Generator

[![Linux Build Status](https://img.shields.io/travis/clytras/afm-python.svg?style=flat)](https://travis-ci.org/clytras/afm-python.svg?branch=master)


Validate and generate Greek TIN (*Tax Identification Number*) / AFM (*Αριθμός Φορολογικού Μητρώου*). Generation function can create valid or invalid numbers including parameters for old format, individuals, legal entities and repet tolerance digits control.

## Online demo and presentation

https://lytrax.io/blog/projects/greek-tin-validator-generator

## Installation

```
pip install lytrax-afm
```

## Usage

Import functions:

```python
from lytrax_afm import validateAFM, \
    generateAFM, \
    generateValidAFM, \
    generateInvalidAFM
```

Validate a number:

```python
>>> validate_afm("090000045")
True

>>> validate_afm("123456789")
False
```

Generate a valid number:

```python
>>> generate_valid_afm()
'731385437'
```

Generate an invalid number:

```python
>>> generate_invalid_afm()
'853003357'
```

## API

**validate_afm**
* `afm: str` - A string to be check if it's a valid AFM
* `extended_result: bool, optional` - Return extended object result if True, single boolean otherwise (default is False)
* **Returns**: `str` or `dict` (Dictionary with `'valid': boolean` and `'error': str ('length' or 'nan' or 'zero' or 'invalid')`)

Example:
```python
>>> validate_afm("ab1234", extended_result=True)
{'valid': False, 'error': 'length'}
```

**generate_afm**
* `force_first_digit: int, optional` - If specified, overrides all pre99, legalEntity and individual (default is None)
* `pre99: bool, optional` - Για ΑΦΜ πριν από 1/1/1999 (ξεκινάει με 0),
  (if True, overrides both legal_entity and individual)
  (default is False)
* `individual: bool, optional` - Φυσικά πρόσωπα, (ξεκινάει με 1-4) (default is False)
* `legal_entity: bool, optional` - Νομικές οντότητες (ξεκινάει με 7-9) (default is False)
* `repeat_tolerance : int, optional` - Number for max repeat tolerance
  (0 for no repeats, unspecified for no check)
  (default is None)
* `valid: bool, optional` - Generate valid or invalid AFM (default is True)
* **Returns**: `str` - A valid or invalid 9 digit AFM number

Example:
```python
>>> generate_afm(force_first_digit=3, repeat_tolerance=1, valid=True)
'335151580'
```

**generate_valid_afm** - Same as `generate_afm` with `valid` parameter force and override to `True`
* **Returns**: `str` - A valid 9 digit AFM number

Example:
```python
>>> generate_valid_afm(pre99=True)
'013583460'
```

**generate_invalid_afm** - Same as `generate_afm` with `valid` parameter force and override to `False`
* **Returns**: `str` - An invalid 9 digit AFM number

Example:
```python
>>> generate_invalid_afm(legal_entity=True)
'780300643'
```

## Test

Clone this repository, run test:

```
git clone https://github.com/clytras/afm-python.git && cd afm-python
python -m unittest discover -s './test' -v
```

## Changelog

See [CHANGELOG](https://github.com/clytras/afm-python/blob/master/CHANGELOG.md)


## License

MIT License - see the [LICENSE](https://github.com/clytras/afm-python/blob/master/LICENSE) file for details
