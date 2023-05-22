# RSA
# Input a string and covert it into numbers 
def convert_string_to_number(input_string):
    numbers = []

    for char in input_string:
        char = char.upper()  # Convert the character to uppercase
        if char.isalpha():
            number = ord(char) - ord('A') + 1
            numbers.append(str(number).zfill(2))  # Pad single-digit numbers with leading zeros

    joined_number = int("".join(numbers))

    return joined_number

input_string = input("Enter a string: ")
number = convert_string_to_number(input_string)

print("Message Number:", number)


# Prime numbers 
def calculate_n(p, q, r):
    n = p * q * r
    print("p =", p)
    print("q =", q)
    print("r =", r)
    return n

p = int(input("Enter the first prime number (p): "))
q = int(input("Enter the second prime number (q): "))
r = int(input("Enter the third prime number (r): "))

n = calculate_n(p, q, r)

print("n:", n)

# Calculation of N (similar to the calculation of phi of (n))


def calculate_N(p, q, r):
    N = (p ** 2 - 1) * (q ** 2 - 1) * (r ** 2 - 1)
    return N

N = calculate_N(p, q, r)

print("N:", N)


# clacutaions of matrix modifications

def create_matrix(message, n):
    # Split the message into four separate numbers
    m1 = int(message[:2])
    m2 = int(message[2:4])
    m3 = int(message[4:6])
    m4 = int(message[6:8])

    # Ensure that each message number is smaller than n
    m1 %= n
    m2 %= n
    m3 %= n
    m4 %= n

    # Create the matrix M
    M = [[m1, m2], [m3, m4]]

    return M

# Predefined values for the message number and n
message_number = "01130114"
number = str(number)
print(number)
n = 105

# Create the matrix using the predefined values
matrix = create_matrix(message_number, n)

print("Matrix M:")
for row in matrix:
    print(row)


# calculation for e and f 


import random
from math import gcd

def select_e(n):
    while True:
        e = random.randint(2, n-1)  # Select a random value for e
        if gcd(e, n) == 1:  # Check if e is coprime with n
            return e

def select_f(n, e):
    while True:
        f = random.randint(2, n-1)  # Select a random value for f
        if f != e and gcd(f, n) == 1:  # Check if f is coprime with n and not equal to e
            return f

# Predefined value for n
n = 100

# Select e and f
e = select_e(n)
f = select_f(n, e)

print("Selected e: [PUBLIC KEY 1] :", e)
print("Selected f: [PUBLIC KEY 2] :", f)


# calculation of d and g 

def calculate_inverse(a, n):
    t = 0
    new_t = 1
    r = n
    new_r = a

    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r

    if r > 1:
        return None  # The inverse does not exist
    if t < 0:
        t += n

    return t

# Predefined values for e and N
# e = 7
# N = 40

# Calculate d and g
d = calculate_inverse(e, N)
g = calculate_inverse(f, N)

print("Calculated d:", d)
print("Calculated g:", g)

#Calculation of Cipher text

from mpmath import mp

# Set the desired precision
mp.dps = 110000

# Function to raise a 2x2 matrix to a given power
def matrixPower(A, power):
    result = A

    for i in range(1, power):
        result = result @ A
    return result

# A = mp.matrix([[1,13], [1,14]])
matrix = mp.matrix


print("ENCRYPTION\n")

import numpy as np

def calculate_ciphertext(M, e, f, n):
    M_mod = np.mod(M, n)
    C = np.linalg.matrix_power(M_mod, e) % n  # Calculate (M^e mod n)
    C = np.linalg.matrix_power(C, f) % n  # Calculate (C^f mod n)
    return C

# Predefined values for the matrix M, e, f, and n
M = np.array([[1, 13], [1,14]])   
e = 29    
f = 101    
n = 105   

# Calculate the ciphertext
ciphertext = calculate_ciphertext(M, e, f, n)

print("Ciphertext:")
print(ciphertext)


print("\n\n\n")

# Calucation Plain text 
print("DECRYPTION\n")

import numpy as np

def calculate_plaintext(C, g, d, n):
    C_mod = np.mod(C, n)
    P = np.linalg.matrix_power(C_mod, g) % n  # Calculate (C^g mod n)
    P = np.linalg.matrix_power(P, d) % n  # Calculate (P^d mod n)
    return P

# Predefined values for the matrices C, g, d, and n
# C = np.array([[5, 6], [7, 8]])  # ciphertext
g = 365
d = 1589
# n = 221

# Calculate the plaintext
plaintext = calculate_plaintext(ciphertext, g, d, n)

print("Plaintext:")
print(plaintext)



