Gauss-Jordan Elimination Method in Python
A beginner-friendly Python 3 implementation of the Gauss-Jordan Elimination Method for solving systems of linear equations.

The program converts an augmented matrix into Reduced Row-Echelon Form (RREF) using elementary row operations. It can identify whether a system has a unique solution, infinitely many solutions, or no solution.
Project structure
Gauss-Jordan-Elimination-Python/
├── README.md
├── gauss_jordan.py
└── LICENSE
What is the Gauss-Jordan method?
Gauss-Jordan elimination is a linear algebra technique used to solve systems of linear equations. It applies elementary row operations until each pivot column has a leading 1 and zeros everywhere else.

The three elementary row operations are:
1. Row swapping: interchange two rows.
2. Row scaling: multiply a row by a non-zero constant.
3. Row replacement: add or subtract a multiple of one row from another row.
Mathematical example
Consider this system:
2y + z       = 4
x + y + 2z   = 6
2x + y + z   = 7
Its augmented matrix is:
[ 0  2  1 | 4 ]
[ 1  1  2 | 6 ]
[ 2  1  1 | 7 ]
After applying Gauss-Jordan elimination, the RREF matrix is:
[ 1  0  0 | 2.2 ]
[ 0  1  0 | 1.4 ]
[ 0  0  1 | 1.2 ]
Therefore:
x = 2.2
y = 1.4
z = 1.2
Requirements
- Python 3.8 or later
- No external Python libraries are required
How to run
1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run:
python gauss_jordan.py
On some systems, use:
python3 gauss_jordan.py
Sample output
GAUSS-JORDAN ELIMINATION

Original augmented matrix:
[     0.0000      2.0000      1.0000 |     4.0000 ]
[     1.0000      1.0000      2.0000 |     6.0000 ]
[     2.0000      1.0000      1.0000 |     7.0000 ]

Reduced row-echelon form (RREF):
[     1.0000      0.0000      0.0000 |     2.2000 ]
[     0.0000      1.0000      0.0000 |     1.4000 ]
[     0.0000      0.0000      1.0000 |     1.2000 ]

Result:
Unique solution exists.
x1 = 2.2000
x2 = 1.4000
x3 = 1.2000
Types of results
The program identifies three possible cases:
Result	Meaning
Unique solution	Exactly one solution exists
Infinite solutions	One or more variables are free
No solution	The equations are inconsistent


How to use your own equations
Edit the augmented_matrix variable inside main() in gauss_jordan.py.

For example, for:
x + y = 5
2x + y = 8
Use:
augmented_matrix = [
    [1, 1, 5],
    [2, 1, 8]
]
Each row contains the coefficients of the variables, followed by the equation's constant. Keep the variable order consistent across all rows.
Concepts covered
- Linear Algebra
- Matrices and augmented matrices
- Elementary row operations
- Pivot elements and row swapping
- Reduced Row-Echelon Form (RREF)
- Systems of linear equations
- Unique, infinite, and inconsistent solutions
Applications in Data Science
Gauss-Jordan elimination is useful for learning the linear algebra behind:
- Systems of linear equations
- Matrix operations and matrix inversion
- Linear regression concepts
- Numerical methods and scientific computing
In practical data science, large systems are generally solved using optimized numerical linear algebra libraries rather than manually applying Gauss-Jordan elimination.
Limitations
- Floating-point arithmetic can introduce small numerical errors.
- The tolerance eps is used to treat very small values as zero.
- This educational implementation is intended for learning and small systems, not large-scale numerical computation.
License
This project is released under the MIT License. See the LICENSE file.
If this project helped you understand Gauss-Jordan elimination, consider giving the repository a star!
