from io import open
import re


def transform_values_to_touples(values):
    if values != "no other bags.":
        list_values = []
        for detail in values.split(', '):
            list_values.append(
                (values[0], re.sub('((\ bag\.?$)|(\ bags\.?$))', '', detail)[2:]))
        return list_values
    return None


def transform_rule_to_dict(rule):
    key, values = rule.split(' bags contain ')
    return {key: transform_values_to_touples(values)}


rules = list()
with open("puzzleInput_test.txt", "r") as fp:
    rules = [rule.rstrip() for rule in fp]

for rule in rules:
    print(
        f"rule: {transform_rule_to_dict(rule)}")
