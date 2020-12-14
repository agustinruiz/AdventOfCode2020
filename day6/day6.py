from io import open


def calculate_group_declaration(group_declarations):
    declarations_union = set()
    for passenger_declaration in group_declarations:
        declarations_union = declarations_union.union(passenger_declaration)
    return len(declarations_union)


def sum_of_questions_groups(groups_declarations):
    sum_of_questions = 0
    for group_declarations in groups_declarations:
        sum_of_questions += calculate_group_declaration(group_declarations)
    return sum_of_questions


groups_declarations = list()
with open("puzzleInput.txt", "r") as fp:
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
print(sum_of_questions_groups(groups_declarations))
