from sympy import Symbol, Eq, rem
import sys

# Create symbols for the dividend, divisor, and remainder
dividend = Symbol('dividend')
divisor = Symbol('divisor')
remainder = Symbol('remainder')

# Set the recursion limit to accommodate large numbers
sys.setrecursionlimit(5000)

# Function to calculate the remainder
def calculate_remainder(dividend_value, divisor_value):
    # Create an equation for the remainder calculation
    eq = Eq(remainder, rem(dividend, divisor))

    # Substitute the actual values into the equation
    eq = eq.subs([(dividend, dividend_value), (divisor, divisor_value)])

    # Solve the equation and get the remainder
    result = eq.rhs.evalf()

    return result

# Accept the dividend and divisor as input
dividend_input = input("Enter the dividend: ")
divisor_input = input("Enter the divisor: ")

# Calculate the remainder
result = calculate_remainder(dividend_input, divisor_input)

print("Remainder:", result)
