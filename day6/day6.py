from io import open


def find_group_set_union(group_declarations):
    declarations_union = set()
    for passenger_declaration in group_declarations:
        declarations_union = declarations_union.union(passenger_declaration)
    return len(declarations_union)


def find_group_set_intersection(group_declarations):
    declarations_union = set(group_declarations[0])
    for passenger_declaration in group_declarations[1:]:
        declarations_union = declarations_union.intersection(
            passenger_declaration)
    return len(declarations_union)


def sum_questions(groups_declarations, function_criteria):
    sum_of_questions = 0
    for group_declarations in groups_declarations:
        sum_of_questions += function_criteria(group_declarations)
    return sum_of_questions


groups_declarations = list()
with open("puzzleInput_test.txt", "r") as fp:
    group_declarations = list()
    for row in fp:
        if row != "\n":
            row2 = row.rstrip()
            group_declarations.append(row2)
        else:
            groups_declarations.append(group_declarations)
            group_declarations = list()
    if group_declarations:
        groups_declarations.append(group_declarations)

print(groups_declarations)
print(
    f"Sum of anyone yes questions: {sum_questions(groups_declarations,find_group_set_union)}")
print(
    f"Sum of everyone yes questions: {sum_questions(groups_declarations,find_group_set_intersection)}")
