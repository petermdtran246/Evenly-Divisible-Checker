# Evenly Divisible Checker
This project contains a Python function that asks the user to input two positive integers and returns True if either integer evenly divides the other. The function will keep asking for valid inputs until the user provides two positive integers. The result is displayed in the calling function.

## Function Definition
The function is_evenly_divisible() will prompt the user to input two positive integers and will return True if either integer evenly divides the other. If the inputs are not valid, it will continue to prompt the user until valid inputs are provided.

## Algorithm

1. Initialize a while loop that runs indefinitely.
2. Use a try...except block to handle invalid inputs.
3. Prompt the user to input two positive integers.
4. Validate that both inputs are positive integers.
5. Check if either number evenly divides the other:
  -  If num1 % num2 == 0 or num2 % num1 == 0, return True.
  -  Otherwise, print a message and continue the loop.
6. Handle invalid inputs (non-positive integers or non-integer values) and continue the loop.
7. Return and print the result outside the function.
