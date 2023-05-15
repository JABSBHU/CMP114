# Get the list of numbers from the user
numbers = input("Enter a list of numbers, separated by spaces: ").split()

# Convert the input strings to integers
numbers = [int(num) for num in numbers]

# Calculate the sum of the numbers
sum_of_numbers = sum(numbers)

# Print the result
print("The sum of the numbers is:", sum_of_numbers)

    