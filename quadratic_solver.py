"""
File: quadratic_solver.py
Name: 姜譿允
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	a : int
	b : int
	c : int
	"""
	print("stanCode Quadratic Solver!")
	a = int(input("Enter a : "))
	b = int(input("Enter b : "))
	c = int(input("Enter c : "))
	discriminant = b * b - 4 * a * c
	if discriminant > 0:
		x1 = float(-b + math.sqrt(discriminant)) / 2 * a
		x2 = float(-b - math.sqrt(discriminant)) / 2 * a
		print("Two roots: " +str(x1) + str(x2))
	elif discriminant == 0:
		x1 = float(-b + math.sqrt(discriminant)) / 2 * a
		x2 = float(-b - math.sqrt(discriminant)) / 2 * a
		print("one root: " + str(x1))
	else:
		print("No real roots")



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
