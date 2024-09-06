#!/usr/bin/python3
import sys

def factorial(n):
	"""
	The factorial mathematical function.

	Parameters:
		n (int): Positive integer to calculate the factorial of
 
 	Returns:
		int: Result of n! (factorial of n)
	"""
	if n <= 1:
		return 1
	else:
		return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)
