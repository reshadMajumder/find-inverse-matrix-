
def print_matrix(mat):
    for row in mat:
        print(row)

def augment_identity(matrix):
    n = len(matrix)
    identity_matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    augmented_matrix = [row + identity_matrix[i] for i, row in enumerate(matrix)]
    return augmented_matrix

def normalize_row(row, pivot_element):
    return [x / pivot_element for x in row]

def eliminate(row_to_modify, pivot_row, factor):
    return [x - factor * y for x, y in zip(row_to_modify, pivot_row)]

def inverse_matrix(matrix):
    
    n = len(matrix)

    augmented_matrix = augment_identity(matrix)

    print("\nOriginal Matrix:")
    print_matrix(matrix)
    print("\nAugmented Matrix:")
    print_matrix(augmented_matrix)

    for i in range(n):
        try:
            pivot_row_index = max(range(i, n), key=lambda j: abs(augmented_matrix[j][i]))
            augmented_matrix[i], augmented_matrix[pivot_row_index] = augmented_matrix[pivot_row_index], augmented_matrix[i]

            pivot_element = augmented_matrix[i][i]
            augmented_matrix[i] = normalize_row(augmented_matrix[i], pivot_element)

            print(f"\nStep {i + 1} - normalizing Row {i + 1} (Divide Row {i + 1} by {pivot_element}):")
            print_matrix(augmented_matrix)

            for j in range(n):
                if i != j:
                    factor = augmented_matrix[j][i]
                    augmented_matrix[j] = eliminate(augmented_matrix[j], augmented_matrix[i], factor)

                    print(f"\nStep {i + 1} - Eliminating Row {i + 1} from Row {j + 1} (Multiply Row {i + 1} by {factor} and subtract from Row {j + 1}):\n")
                    print_matrix(augmented_matrix)

        except ZeroDivisionError:
            print("\nError: This matrix is singular and cannot be inverted.")
            return

    inverse = [row[n:] for row in augmented_matrix]

    print("\nInverse Matrix:")
    print_matrix(inverse)

try:
    n = int(input("enter the size of the matrix: "))
    print(f"Enter the {n}x{n} elements of the matrix:")

    matrix = []

    for _ in range(n):
        row = input()
        row_values = [int(value) for value in row.split()]
        matrix.append(row_values)

    inverse_matrix(matrix)
    print("\n\nplease number Barai diyen sir 🙏\n")

except ValueError:
    print("\ninvalid input values. ")

