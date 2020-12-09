from io import open
import pdb


def calculate_row(boarding_pass):
    row = 0
    row_chars = boarding_pass[:7]
    for index, character in enumerate(row_chars[::-1]):
        row += (2**index if character == 'B' else 0)
    return row


def calculate_column(boarding_pass):
    column = 0
    column_chars = boarding_pass[-3:]
    for index, character in enumerate(column_chars[::-1]):
        column += 2**index if character == 'R' else 0
    return column


def calculate_boarding_pass_id(boarding_pass):
    row = calculate_row(boarding_pass)
    column = calculate_column(boarding_pass)
    return row * 8 + column


def find_max_id(boarding_passes):
    max_id = 0
    for boarding_pass in boarding_passes:
        pass_id = calculate_boarding_pass_id(boarding_pass)
        if max_id < pass_id:
            max_id = pass_id
    return max_id


def find_free_seats(boarding_passes):
    passes_ids = list(map(calculate_boarding_pass_id, boarding_passes))
    free_spaces = []
    for id in range(len(passes_ids)):
        if id not in passes_ids:
            free_spaces.append(id)
    return free_spaces


with open("puzzleInput.txt", "r") as fp:
    boarding_passes = [line.rstrip() for line in fp]

print(f"Max ID: {find_max_id(boarding_passes)}")
print(f"Seat ID: {find_free_seats(boarding_passes)}")
