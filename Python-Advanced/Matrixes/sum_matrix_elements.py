def read_matrix_func():

    rows, cols = map(int, input().split(', '))
    current_matrix = []

    for r in range(rows):
        row_data = list(map(int, input().split(', ')))
        current_matrix.append(row_data)

    return current_matrix


matrix = read_matrix_func()

# comprehension:
matrix_el_sum = sum([sum(current_el) for current_el in matrix])

# matrix_el_sum = 0

# for el in range(len(matrix)):
#     current_row = matrix[el]
#     matrix_el_sum += sum(current_row)

print(matrix_el_sum)
print(matrix)