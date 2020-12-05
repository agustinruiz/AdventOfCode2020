from io import open
import pdb
import re


def is_passport_valid(passport):
    result = False
    if len(passport) == 7:
        result = 'cid' not in passport
    elif len(passport) == 8:
        result = True
    print(f"{passport} len: {len(passport)} result: {result}")
    return result


def validate_byr(byr):
    return '1920' <= byr <= '2002'


def validate_iyr(iyr):
    return '2010' <= iyr <= '2020'


def validate_eyr(eyr):
    return '2020' <= eyr <= '2030'


def validate_hgt(hgt):
    result = False
    if hgt[-2:] == 'cm':
        result = '150' <= hgt[:-2] <= '193'
    elif hgt[-2:] == 'in':
        result = '59' <= hgt[:-2] <= '76'
    return result


def validate_hcl(hcl):
    return bool(re.match(r"#[0-9a-f]{6}", hcl))


def validate_ecl(ecl):
    valid_values = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return ecl in valid_values


def validate_pid(pid):
    return bool(re.match(r"[0-9]{9}", pid))


def validate_passports_fields(passport):
    return (
        validate_byr(passport['byr'])
        and validate_iyr(passport['iyr'])
        and validate_eyr(passport['eyr'])
        and validate_hgt(passport['hgt'])
        and validate_hcl(passport['hcl'])
        and validate_ecl(passport['ecl'])
        and validate_pid(passport['pid'])
    )


def is_passport_valid2(passport):
    result = False
    if len(passport) == 7:
        result = ('cid' not in passport
                  and validate_passports_fields(passport)
                  )
    elif len(passport) == 8:
        result = validate_passports_fields(passport)
    print(f"{passport} len: {len(passport)} result: {result}")
    return result


passports_list = []
with open("puzzleInput.txt", "r") as fp:
    passport_dict = dict()
    for row in fp:
        if row != "\n":
            row2 = row.rstrip()
#            print(dict([tuple(field.split(":")) for field in row2.split(" ")]))
            passport_dict.update(
                dict([tuple(field.split(":")) for field in row2.split(" ")]))
        else:
            passports_list.append(passport_dict)
            passport_dict = dict()

valid_passports = 0
for passport in passports_list:
    if is_passport_valid2(passport):
        valid_passports += 1

print(f"Number of valid password: {valid_passports}")
