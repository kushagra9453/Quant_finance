import numpy as np

# Q1: Matrix inverse
A = np.array([[4, 7], [2, 6]])
inv_A = np.linalg.inv(A)
print(inv_A)  

# Q2: Determinant
A = np.array([[1, 2], [3, 4]])
det = np.linalg.det(A)
print(det)  

# Q3: Solve linear system
# 3x + y = 9
# x + 2y = 8
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = np.linalg.solve(A, b)
print(x)  

# Q4: Eigenvalues and eigenvectors
A = np.array([[2, 1], [1, 2]])
eigvals, eigvecs = np.linalg.eig(A)
print("Eigenvalues:", eigvals)
print("Eigenvectors:\n", eigvecs)

# Q5: Matrix multiplication using @
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = A @ B
print(C) 

# Q6: Trace (sum of diagonal)
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
trace = np.trace(A)
print(trace)  

# Q7: Check if matrix is singular (determinant near zero)
A = np.array([[2, 2], [1, 1]])
det = np.linalg.det(A)
print(f"Determinant: {det:.2f}")  
is_singular = np.isclose(det, 0)
print(is_singular)  

# Q8: Extract diagonal elements
A = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
diag = np.diag(A)
print(diag) 

# Q9: Create identity matrix of size 4
I = np.eye(4)
print(I)  

# Q10: Raise matrix to power 2 (matrix multiplication with itself)
A = np.array([[1, 2], [3, 4]])
A_squared = np.linalg.matrix_power(A, 2)
print(A_squared) 