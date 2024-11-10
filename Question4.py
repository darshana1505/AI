# question - 4
import numpy as np

A = np.array([[1, 2, 3],
              [0, 1, 4],
              [5, 6, 0]])

A_inv = np.linalg.inv(A)

AA_inv = np.dot(A, A_inv)
A_invA = np.dot(A_inv, A)

print("A * A_inv:\n", AA_inv)
print("A_inv * A:\n", A_invA)