def creating_matrix_func():
    rows = int(input())
    current_matrix = []

    for r in range(rows):
        row_data = list(input())
        current_matrix.append(row_data)

    return current_matrix


def searching_for_special_symbol_func(current_matrix, symbol):
    for row in range(len(current_matrix)):
        for col in range(len(current_matrix[row])):
            current_element = current_matrix[row][col]
            if current_element == special_symbol:
                return row, col


def print_func(data, symbol):
    if data:
        print(data)

    else:
        print(f'{symbol} does not occur in the matrix')


matrix = creating_matrix_func()
special_symbol = input()
special_symbol_search = searching_for_special_symbol_func(matrix, special_symbol)
print_func(special_symbol_search, special_symbol)