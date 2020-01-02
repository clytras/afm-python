from ._validation import validate_afm
from ._generation import generate_valid_afm, generate_invalid_afm

def main():
    gen_valid()
    print()
    gen_invalid()

def gen_valid():
    print("Demo: Generate valid numbers\n")

    report("(default)", generate_valid_afm())
    report("pre99", generate_valid_afm(pre99=True))
    report("legal_entity", generate_valid_afm(legal_entity=True))
    report("individual", generate_valid_afm(individual=True))
    report("repeat_tolerance:0", generate_valid_afm(repeat_tolerance=0))

def gen_invalid():
    print("Demo: Generate invalid numbers\n")

    report("(default)", generate_invalid_afm())
    report("pre99", generate_invalid_afm(pre99=True))
    report("legal_entity", generate_invalid_afm(legal_entity=True))
    report("individual", generate_invalid_afm(individual=True))
    report("repeat_tolerance:0", generate_invalid_afm(repeat_tolerance=0))

def report(label, number):
    print("%s %s %s" % (label, number, validator(validate_afm(number))))

def validator(valid):
    return '(valid)' if valid else '(invalid)'

if __name__ == "__main__":
    main()
