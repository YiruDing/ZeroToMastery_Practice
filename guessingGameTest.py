import unittest
import script

class TestGame(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = script.run_guess(answer,guess)
        self.assertTrue(result)

    def test_input_wrong_number(self):
        # answer = 5
        # guess = 0
        result = script.run_guess(5,0)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = script.run_guess(5,'Lalala')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()