def is_evenly_divisible():
   # Create a loop to repeatedly ask for valid input
   while True:
      try:
         # Prompt user to input two positive integers - greater than 0 (1,2,3,4,....)
         num1 = int(input('Enter the first integer: '))
         num2 = int(input('Enter the second integer: '))
         # If...Else condition. Check if both nums are positive integers.
         if num1 > 0 and num2 > 0:
            if num1 % num2 == 0 or num2 % num1 == 0:
               return True
            else:
               print('The numbers are not divisible by each other. Please try again.')
         else:
            print('Invalid Input. Please enter positive integers again.')
      except ValueError:
         print('Invalid Input. Please enter valid positive integers.')
# Call a function
result = is_evenly_divisible()
print(result)







