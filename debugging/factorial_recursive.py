#!/usr/bin/python3
import sys

# Recursive factorial function
def factorial(n):
	# Return 1 if 1 or 0
	if n <= 1:
		return 1
	else:
		# Multiply the current number with the factorial of the previous one
		return n * factorial(n - 1)

# f is factorial of the input argument (converted to int beforehand)
f = factorial(int(sys.argv[1]))
# Print the result
print(f)
