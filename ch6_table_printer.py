"""
https://automatetheboringstuff.com/2e/chapter6/
Write a function named printTable() that takes a list of lists of strings
and displays it in a table with each column right-justified.

Assume that all the inner lists will contain the same number of strings.
"""

# Assumes data is a valid list of lists of strings
def print_table(table_data: list):
    col_width = [0] * len(table_data)
    num_strings = len(table_data[0])

    for x in range(len(table_data)):
        for data in table_data[x]:
            if col_width[x] < len(data):
                col_width[x] = len(data)
        # Add one to the maximum length for spacing between columns
        col_width[x] += 1

    # Build and output each row of the table
    for x in range(num_strings):
        row = ""
        for y in range(len(table_data)):
            row += table_data[y][x].rjust(col_width[y])

        print(row)


table_data = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "mongoose"],
]
print_table(table_data)
