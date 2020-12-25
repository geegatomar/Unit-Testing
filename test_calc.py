import unittest                               # The unit testing framework that we are importing
import calc

print(calc)

# Now we need to create some test cases. In order to do that, we first need to create a test class that  
# INHERITS from unittest.TestCase


class TestCalc(unittest.TestCase):

    def test_add(self):                      # imp convention for unittest framework to write test_ for all methods
        result = calc.add(10, 5)
        expected_result = 15
        self.assertEqual(result, expected_result)

