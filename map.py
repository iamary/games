# Define a function to apply
def square(x):
    return x * x

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use the map function to apply the square function to each number in the list
squared_numbers = map(square, numbers)

# Convert the result to a list and print it
print(list(squared_numbers))