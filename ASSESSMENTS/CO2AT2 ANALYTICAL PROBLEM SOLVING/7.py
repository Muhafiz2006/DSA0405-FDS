from scipy import linalg
A = [[3, 2], [1, 2]]
B = [5, 5]
solution = linalg.solve(A, B)
print("Solution:", solution)
