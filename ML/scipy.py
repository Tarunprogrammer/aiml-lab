from scipy import linalg
from scipy import special
from scipy import constants
import numpy as np

# Print constants
print("Seconds in a minute:", constants.minute)
print("Seconds in an hour:", constants.hour)
print("Length of an inch in meters:", constants.inch)
print("Volume of a liter in cubic meters:", constants.liter)

# Dynamic input for exponentiation
exp_input = float(input("Enter the exponent for 10^x: "))
print(f"10^{exp_input} =", special.exp10(exp_input))

# Dynamic input for angles
angle = float(input("Enter an angle for sine and cosine (in degrees): "))

# Calculate sine and cosine
print(f"sin({angle} degrees):", special.sindg(angle))
print(f"cos({angle} degrees):", special.cosdg(angle))

# Matrix input
rows = int(input("Enter the number of rows for the matrix: "))
cols = int(input("Enter the number of columns for the matrix: "))

elements = list(map(float, input(f"Enter {rows * cols} elements separated by spaces: ").split()))

# Convert to NumPy matrix
mat = np.array(elements).reshape((rows, cols))

print("\nMatrix:")
print(mat)

# Determinant calculation
if rows == cols:
    det = linalg.det(mat)
    print(f"\nDeterminant of the matrix is: {det}")
else:
    print("Determinant can only be calculated for square matrices.")