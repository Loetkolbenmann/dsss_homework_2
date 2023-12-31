import unittest
from math_quiz import get_random_int, get_random_arithmetic_operator, generate_problem


class TestMathGame(unittest.TestCase):

    def test_get_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_arithmetic_operator(self):
        # Test if returned strings are '+', '-' or '/'
        for _ in range(1000):  
            rand_operator = get_random_arithmetic_operator()
            self.assertTrue(rand_operator == '+' or rand_operator == '-' or rand_operator == '*')
        

    def test_generate_problem(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (4, 2, '-', '4 - 2', 2),
                (3, 4, '*', '3 * 4', 12)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = generate_problem(num1, num2, operator)
                self.assertTrue(problem == expected_problem and answer == expected_answer)

if __name__ == "__main__":
    unittest.main()
