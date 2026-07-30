from scipy.optimize import minimize
def objective(x):
 return x**2 + 4
result = minimize(objective, x0=5)
print("Minimum value of x:", result.x)
