import numpy as np

# Creating arrays
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])

# Array operations
sum_ab = a + a
product_ab = a * a

# Array slicing
slice_a = a[1:3]

# Array reshaping
reshaped_b = b.reshape((3, 2))

# Array statistics
mean_b = np.mean(b)
std_b = np.std(b)

# Linear algebra
dot_product = np.dot(a, a)
inverse_b = np.linalg.inv(np.array([[1, 2], [3, 4]]))

print("Array a:", a)
print("Array b:", b)
print("Sum of a and a:", sum_ab)
print("Product of a and a:", product_ab)
print("Slice of a:", slice_a)
print("Reshaped b:", reshaped_b)
print("Mean of b:", mean_b)
print("Standard deviation of b:", std_b)
print("Dot product of a and a:", dot_product)
print("Inverse of a 2x2 matrix:", inverse_b)