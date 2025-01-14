""" In this programming assignment you will implement one or more of the integer multiplication algorithms described in lecture.

To get the most out of this assignment, your program should restrict itself to multiplying only pairs of single-digit numbers.
You can implement the grade-school algorithm if you want, but to get the most out of the assignment you'll want to implement
recursive integer multiplication and/or Karatsuba's algorithm.

So: what's the product of the following two 64-digit numbers?

3141592653589793238462643383279502884197169399375105820974944592
2718281828459045235360287471352662497757247093699959574966967627
"""

from math import floor, ceil


def karatsuba(num1: int, num2: int) -> int:
    if num1 < 10 or num2 < 10:
        return num1 * num2 # fall back to traditional multiplication

    # Calculates the size of the numbers.
    m = max(len(str(num1)), len(str(num2)))
    m2 = ceil(m / 2)

    # Split the digit sequences in the middle.
    high1, low1 = num1 // 10 ** m2, num1 % 10 ** m2
    high2, low2 = num2 // 10 ** m2, num2 % 10 ** m2

    # 3 recursive calls made to numbers approximately half the size.
    z0 = karatsuba(high1, high2)
    z1 = karatsuba(low1, low2)
    z2 = karatsuba(low1 + high1, low2 + high2)

    return (z0 * (10 ** (m2 * 2))) + ((z2 - z1 - z0) * 10 ** m2) + z1


first_num = 3141592653589793238462643383279502884197169399375105820974944592
second_num = 2718281828459045235360287471352662497757247093699959574966967627

result = karatsuba(first_num, second_num)

if result != (first_num * second_num):
    print("Karatsuba multiplication function doesn't work properly.")
