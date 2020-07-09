'''
In mathematics, a matrix (plural matrices) is a rectangular array of numbers. Matrices have many applications in programming, from performing transformations in 2D space to machine learning.

One of the most useful operations to perform on matrices is matrix multiplication, which takes a pair of matrices and produces another matrix – known as the dot product. Multiplying matrices is very different to multiplying real numbers, and follows its own set of rules.

Unlike multiplying real numbers, multiplying matrices is non-commutative: in other words, multiplying matrix a by matrix b will not give the same result as multiplying matrix b by matrix a.

Additionally, not all pairs of matrix can be multiplied. For two matrices to be multipliable, the number of columns in matrix a must match the number of rows in matrix b.

There are many introductions to matrix multiplication online, including at Khan Academy, and in the classic MIT lecture series by Herbert Gross.

To complete this kata, write a function that takes two matrices - a and b - and returns the dot product of those matrices. If the matrices cannot be multiplied, return -1 for JS/Python, or null for Java.

Each matrix will be represented by a two-dimensional list (a list of lists). Each inner list will contain one or more numbers, representing a row in the matrix.

'''


def getMatrixProduct(a, b):
    rows_A = len(a)
    cols_A = len(a[0])
    rows_B = len(b)
    cols_B = len(b[0])

    if cols_A != rows_B:
        return -1
    else:
        C = [[0 for row in range(cols_B)] for col in range(rows_A)]
        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    C[i][j] += a[i][k] * b[k][j]
        return C  
