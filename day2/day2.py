from io import open
import re


def is_password_valid_for_policy1(policy_and_password):
    policy, password = policy_and_password.split(':')
    min_max, letter = policy.split(' ')
    minimum, maximum = min_max.split('-')
    letter_count = password.count(letter)
    return int(minimum) <= letter_count <= int(maximum)


def is_password_valid_for_policy2(policy_and_password):
    policy, password = policy_and_password.split(':')
    positions, letter = policy.split(' ')
    position1, position2 = positions.split('-')
    return (password[int(position1)] == letter) ^ (password[int(position2)] == letter)


with open("puzzleInput.txt", "r") as fp:
    lines = [line.rstrip() for line in fp]

validPasswords = list(filter(is_password_valid_for_policy1, lines))
print(f"Valid passwords count with first policy= {len(validPasswords)}")
validPasswords = list(filter(is_password_valid_for_policy2, lines))
# print(validPasswords)
print(f"Valid passwords count with second policy= {len(validPasswords)}")
