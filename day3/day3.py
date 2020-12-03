from io import open
import pdb

with open("puzzleInput.txt", "r") as fp:
    rows = [row.rstrip() for row in fp]


def number_of_chars(rows, right_step, down_step, character):
    row = 0
    column = 0
    total_of_chars = 0
    # pdb.set_trace()
    while row < len(rows)-1:
        if (column + right_step) < len(rows[row]):
            column += right_step
        else:
            column = (column + right_step) - len(rows[row])
        row += down_step
        if rows[row][column] == character:
            total_of_chars += 1
    return total_of_chars


trees1 = number_of_chars(rows, 1, 1, '#')
print(f"Trees 1-1 count: {trees1}")
trees2 = number_of_chars(rows, 3, 1, '#')
print(f"Trees 3-1 count: {trees2}")
trees3 = number_of_chars(rows, 5, 1, '#')
print(f"Trees 5-1 count: {trees3}")
trees4 = number_of_chars(rows, 7, 1, '#')
print(f"Trees 7-1 count: {trees4}")
trees5 = number_of_chars(rows, 1, 2, '#')
print(f"Trees 1-2 count: {trees5}")

print(f"Multiply {trees1*trees2*trees3*trees4*trees5}")
