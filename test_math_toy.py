import unittest

from math_toy import factorial, is_prime, square  # Ensure to import the functions from your script

class TestMathFunctions(unittest.TestCase):

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1, "Factorial of 0 should equal 1")

    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120, "Factorial of 5 should equal 120")

    def test_factorial_initialization_bug(self):
        self.assertNotEqual(factorial(5), 0, "Factorial of 5 shouldn't equal 0")

    def test_is_prime_prime_number(self):
        #Test with a prime numbe that should return True
        self.assertTrue(is_prime(29), "Number 29 is a prime")

    def test_is_prime_non_prime_number(self):
        #Test with a non-prime number that should return False
        self.assertFalse(is_prime(10), "Number 10 is not a prime")

    def test_is_prime_edge_cases(self):
        #Edge cases, like 0 and 1, which are not prime
        self.assertFalse(is_prime(0), "Zero is not prime")
        self.assertFalse(is_prime(1), "One is not prime")

    def test_square_correct_calculation(self):
        #Test that the square of a number is calculated correctly
        self.assertEqual(square(10), 100, "Squaring 10 must produce 100")

    def test_square_bug(self):
        #Test to find the intentional bug that incorrectly adds 1
        self.assertNotEqual(square(10), 101, "Squaring 10 must not yield 101")

if __name__ == '__main__':
    unittest.main()
