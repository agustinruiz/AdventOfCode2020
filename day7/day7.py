from io import open
import re


def transform_values_to_touples(values):
    if values != "no other bags.":
        list_values = []
        for detail in values.split(', '):
            list_values.append(
                (detail[0], re.sub('((\ bag\.?$)|(\ bags\.?$))', '', detail)[2:]))
        return list_values
    return None


def transform_rule_to_dict(rule):
    key, values = rule.split(' bags contain ')
    return {key: transform_values_to_touples(values)}


def bag_can_contain(parent, child, rules):
    value = rules[parent]
    if not value:
        return False
    for count, bag in value:
        if bag == child:
            return True
        if bag_can_contain(bag, child, rules):
            return True
    return False


def number_of_bags_inside(bag, rules):
    value = rules[bag]
    if not value:
        return 0
    number_of_bags = 0
    for bag_count, bag_inside in value:
        number_of_bags += int(bag_count) + int(bag_count) * \
            number_of_bags_inside(bag_inside, rules)
    return number_of_bags


rules = list()
with open("puzzleInput.txt", "r") as fp:
    rules = [rule.rstrip() for rule in fp]

rules_dict = dict()
for rule in rules:
    rules_dict.update(transform_rule_to_dict(rule))


count = 0
for bag in rules_dict:
    if bag_can_contain(bag, 'shiny gold', rules_dict):
        count += 1

print(f"Number of bags that can contain shiny gold: {count}")

print(
    f"Number of bags inside the shiny gold bag: {number_of_bags_inside('shiny gold', rules_dict)}")
