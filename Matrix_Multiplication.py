# Function to take user input for a matrix
def get_matrix_input(rows, columns):
    matrix = []
    print(f"Enter the elements for a {rows}x{columns} matrix:")
    for i in range(rows):
        row = []
        for j in range(columns):
            element = float(input(f"Enter element at position ({i+1},{j+1}): "))
            row.append(element)
        matrix.append(row)
    return matrix

# Function to multiply two matrices
def matrix_multiplication(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Error: Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
        return None

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = 0
            for k in range(len(matrix2)):
                element += matrix1[i][k] * matrix2[k][j]
            row.append(element)
        result.append(row)
    return result

# Get dimensions for the first matrix
rows1 = int(input("Enter the number of rows for the first matrix: "))
cols1 = int(input("Enter the number of columns for the first matrix: "))

# Get dimensions for the second matrix
rows2 = int(input("Enter the number of rows for the second matrix: "))
cols2 = int(input("Enter the number of columns for the second matrix: "))

# Take input for the matrices
matrix1 = get_matrix_input(rows1, cols1)
matrix2 = get_matrix_input(rows2, cols2)

# Perform matrix multiplication
result = matrix_multiplication(matrix1, matrix2)

# Display the result
if result is not None:
    print("Matrix multiplication result:")
    for row in result:
        print(row)
