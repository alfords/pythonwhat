import os
import unittest

from os.path import exists
from unittest.mock import patch

from pythonbackend.Exercise import Exercise
from pythonbackend import utils

import helper

class TestFunctionBase(unittest.TestCase):

  def setUp(self):
    self.data = {
      "DC_PEC": '''
# pec comes here
      ''',
      "DC_CODE": '''
print(5 / 8)
print(7 + 10)
      ''',
      "DC_SOLUTION": '''
print(5 / 8)
print(7 + 10)
'''
    }

  def test_Pass(self):
    self.data["DC_SCT"] = '''
msg = "Don't remove the first statement. It is an example which is coded for you!"
test_operator(1, incorrect_op_msg = msg, incorrect_result_msg = msg, not_found_msg = msg)
test_operator(2, not_found_msg = "You should add a second operation, as instructed.",
  incorrect_op_msg = "Your second operation is wrong, be sure to add `7` to `10`.",
  incorrect_result_msg = "The operation you added should add up to `17`.")
test_function("print", 1)
test_function("print", 2)

success_msg("Great!")
    '''
    self.exercise = Exercise(self.data)
    self.exercise.runInit()
    output = self.exercise.runSubmit(self.data)
    sct_payload = helper.get_sct_payload(output)
    self.assertEqual(sct_payload['correct'], True)
    self.assertEqual(sct_payload['message'], "Great!")

class TestFunctionExerciseNumpy(unittest.TestCase):

  def setUp(self):
    self.data = {
      "DC_PEC": '''
# pec comes here
      ''',
      "DC_CODE": '''
# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np

# Create a 2D Numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)
      ''',
      "DC_SOLUTION": '''
# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np

# Create a 2D Numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)
'''
    }

  def test_Pass(self):
    self.data["DC_SCT"] = '''
msg = "You don't have to change or remove the predefined variables."
test_object("baseball", undefined_msg = msg, incorrect_msg = msg)

test_import("numpy", same_as = False)

test_object("np_baseball", do_eval = False)
test_function("numpy.array", not_called_msg = "Be sure to call [`np.array()`](http://docs.scipy.org/doc/numpy-1.10.0/glossary.html#term-array).",
                             incorrect_msg = "You should call `np.array(baseball)` to make a 2D numpy array out of `baseball`.")
test_object("np_baseball", incorrect_msg = "Assign the correct value to `np_baseball`.")

msg = "Make sure to print out the type of `np_baseball` like this: `print(type(np_baseball))`."
test_function("type", 1, incorrect_msg = msg)
test_function("print", 1, incorrect_msg = msg)

test_function("print", 2, incorrect_msg = "You can print the shape of `np_baseball` like this: `np_baseball.shape`.")

success_msg("Great! You're ready to convert the actual MLB data to a 2D Numpy array now!")
    '''
    self.exercise = Exercise(self.data)
    self.exercise.runInit()
    output = self.exercise.runSubmit(self.data)
    sct_payload = helper.get_sct_payload(output)
    self.assertEqual(sct_payload['correct'], True)
    self.assertEqual(sct_payload['message'], "Great! You're ready to convert the actual MLB data to a 2D Numpy array now!")

class TestFunctionImporting(unittest.TestCase):

  def setUp(self):
    self.data = {
      "DC_PEC": '''
# pec comes here
      ''',
      "DC_CODE": '''
# Open a file
file = open('moby_dick.txt' , 'r') # 'r' is to read only.

# Print it
print(file.read())

# Check whether file is closed
print(file.close)

# Close file
file.close()

# Check whether file is closed
print(file.closed)
      ''',
      "DC_SOLUTION": '''
# Open a file
file = open('moby_dick.txt' , 'r') # 'r' is to read only.

# Print it
print(file.read())

# Check whether file is closed
print(file.closed)

# Close file
file.close()

# Check whether file is closed
print(file.closed)
'''
    }

  def test_Fail(self):
    self.data["DC_SCT"] = '''
test_function("open", incorrect_msg = "Pass the correct arguments to `open()`" )
file_read_msg = "Make sure to print out the contents of the file like this: `print(file.read())`."
test_function("file.read", incorrect_msg = file_read_msg)
test_function("print", 1, args = [], incorrect_msg = file_read_msg)
file_closed_msg = "Make sure to call `print()` the attribute `file.closed` twice, once before you closed the `file` and once after."
test_function("print", 2, incorrect_msg = file_closed_msg)
test_function("print", 3, incorrect_msg = file_closed_msg)
test_expression_output(incorrect_msg = file_read_msg)
test_function("file.close", not_called_msg = "Make sure to close the file, man!")
success_msg("Good job!")
    '''
    self.exercise = Exercise(self.data)
    self.exercise.runInit()
    output = self.exercise.runSubmit(self.data)
    sct_payload = helper.get_sct_payload(output)
    self.assertEqual(sct_payload['correct'], False)
    self.assertEqual(sct_payload['message'], "Make sure to call <code>print()</code> the attribute <code>file.closed</code> twice, once before you closed the <code>file</code> and once after.")

if __name__ == "__main__":
    unittest.main()
