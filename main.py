# Ask user for positive integer
user_input = int(input("Enter a positive integer: "))

# Initialize variables
sum_of_numbers= 0
current_number= 0

# Check if user input is positive
if user_input<= 0:
  print("Please enter a positive integer greater than zero.")
else:
  # Use a while loop to calculate the sum from 0 to the user input
  while current_number <= user_input:
    sum_of_numbers += current_number # Add the current number to the sum
    current_number += 1 # Move to the next number

    # Display the result
    print(f"The sum of numbers from 0 to {user_input} is {sum_of_numbers}.")