"""
Gauss-Jordan Elimination Method
-------------------------------
Solve a system of linear equations using row operations.

Input format:
Each row contains the coefficients of the variables followed by
the right-hand-side constant.

Example:
x + y = 5
2x + y = 8

Augmented matrix:
[
    [1, 1, 5],
    [2, 1, 8]
]
"""

def gauss_jordan(matrix, eps=1e-10):
    """Return the reduced matrix, pivot columns, and solution status."""
    if not matrix or not matrix[0]:
        raise ValueError("The matrix must not be empty.")

    rows = len(matrix)
    cols = len(matrix[0])

    if any(len(row) != cols for row in matrix):
        raise ValueError("All matrix rows must have the same length.")

    variable_count = cols - 1
    if variable_count < 1:
        raise ValueError("Each row must contain at least one variable and one constant.")

    # Work on a copy so the original input is not modified.
    a = [[float(value) for value in row] for row in matrix]

    pivot_row = 0
    pivot_columns = []

    # Process each variable column.
    for col in range(variable_count):
        if pivot_row >= rows:
            break

        # Partial pivoting: choose the row with the largest absolute
        # coefficient in the current column.
        best_row = max(
            range(pivot_row, rows),
            key=lambda r: abs(a[r][col])
        )

        if abs(a[best_row][col]) < eps:
            continue

        # Swap the selected row into the pivot position.
        a[pivot_row], a[best_row] = a[best_row], a[pivot_row]

        # Make the pivot equal to 1.
        pivot = a[pivot_row][col]
        a[pivot_row] = [value / pivot for value in a[pivot_row]]

        # Make every other entry in this pivot column equal to 0.
        for r in range(rows):
            if r == pivot_row:
                continue

            factor = a[r][col]
            if abs(factor) > eps:
                a[r] = [
                    a[r][c] - factor * a[pivot_row][c]
                    for c in range(cols)
                ]

        pivot_columns.append(col)
        pivot_row += 1

    # Check for an inconsistent row: 0x + 0y + ... = non-zero.
    for row in a:
        all_zero_coefficients = all(
            abs(row[c]) < eps for c in range(variable_count)
        )
        if all_zero_coefficients and abs(row[-1]) >= eps:
            return a, pivot_columns, "no_solution", None

    # If at least one variable has no pivot, there is a free variable.
    if len(pivot_columns) < variable_count:
        return a, pivot_columns, "infinite_solutions", None

    # With a pivot in every variable column, the solution is unique.
    solution = [0.0] * variable_count
    for r, col in enumerate(pivot_columns):
        solution[col] = a[r][-1]

    return a, pivot_columns, "unique", solution


def print_matrix(matrix):
    """Print an augmented matrix in a readable format."""
    for row in matrix:
        left = "  ".join(f"{value:10.4f}" for value in row[:-1])
        print(f"[ {left} | {row[-1]:10.4f} ]")


def main():
    # Example system:
    # 2y + z = 4
    # x + y + 2z = 6
    # 2x + y + z = 7
    augmented_matrix = [
        [0, 2, 1, 4],
        [1, 1, 2, 6],
        [2, 1, 1, 7]
    ]

    print("GAUSS-JORDAN ELIMINATION")
    print("\nOriginal augmented matrix:")
    print_matrix(augmented_matrix)

    reduced_matrix, pivots, status, solution = gauss_jordan(augmented_matrix)

    print("\nReduced row-echelon form (RREF):")
    print_matrix(reduced_matrix)

    print("\nResult:")
    if status == "unique":
        print("Unique solution exists.")
        for index, value in enumerate(solution, start=1):
            print(f"x{index} = {value:.4f}")
    elif status == "infinite_solutions":
        print("Infinite solutions exist (one or more free variables).")
    else:
        print("No solution exists (the system is inconsistent).")


if __name__ == "__main__":
    main()
