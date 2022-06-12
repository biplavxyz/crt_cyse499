#!/usr/bin/env python3

print("\033[1;32m=====================================================")
print("Finding The Value Of X Using CRT")
print("=====================================================")

# Given values
a1, a2, a3, m1, m2, m3 = 3, 5, 8, 7, 13, 11

# Calculates M by multiplying m1, m2, m3
M = m1 * m2 * m3
print("Value of M =",M)

print("=====================================================")

# Calculates M1, M2, and M3 by dividing M by m1, m2, and m3 respectively
M1 = int(M / m1)
M2 = int(M / m2)
M3 = int(M / m3)

print("Values of M1, M2, M3 =", M1, M2, M3)

print("=====================================================")

# Calculates inverse of M1, M2, and M3
M1_inv = pow(M1, -1, m1)
M2_inv = pow(M2, -1, m2)
M3_inv = pow(M3, -1, m3)

print("Value of M1_inverse, M2_inverse, M3_inverse = ", M1_inv, M2_inv, M3_inv)

print("=====================================================")

# Value for X is calculated using all the values from above
X = ((a1 * M1 * M1_inv) + (a2 * M2 * M2_inv) + (a3 * M3 * M3_inv)) % M
print("Value of X = ", X)

print("=====================================================")


