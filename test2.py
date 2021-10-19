# Pylint
# pyflakes
# pEP .8

import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print('About to test a funciton')

    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result,15)

    def test_do_stuff2(self):
        test_param = 'srtegrhr'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result,ValueError)
        # == self.assertTrue(isinstance(result,ValueError))
        # Check if the result would be a valueError
    
    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result,'Please enter number')
    
    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result,'Please enter number')

    def tearDown(self):
        print('Cleaning up')

if __name__ == '__main__':
  unittest.main()