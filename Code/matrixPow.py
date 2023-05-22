from mpmath import mp

# Set the desired precision
mp.dps = 110000

# Function to raise a 2x2 matrix to a given power
def matrixPower(A, power):
    result = A

    for i in range(1, power):
        result = result @ A
    return result

A = mp.matrix([[1,13], [1,14]])
power = 365 

# Calculate A^53
result = matrixPower(A, power)

print(f"A^{power}:\n\n\n\n{result}")
