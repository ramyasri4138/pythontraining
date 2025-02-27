# listexa=[]
# n=int(input())
# for i in range(n):
#     value=int(input())
#     listexa.append(value)
# print(listexa)
# The ValueError occurs because the input provided ('1 2') cannot be converted to an integer
# using the int() function. To handle multiple inputs in a single line, you can use the split() 
# method to break the input string into individual components and then convert each component 
# to an integer.
# Create an empty list to store the user input
listexa = []

# Ask the user to enter all numbers separated by spaces
user_input = input("Enter numbers separated by spaces: ")

# Split the input string into individual components
input_values = user_input.split()

# Convert each component to an integer and append it to the list
for value in input_values:
    listexa.append(value)

# Print the list
print("The numbers you entered are:", listexa)

# Print the list without brackets
print("The numbers you entered are:", ' '.join(map(str, listexa)))
# The map(str, listexa) converts each integer in the list to a string.

# The ' '.join(...) method joins the string representations of the integers with a space 
# separator, resulting in a single string without brackets.
# Multiple inputs can be taken, but the method to do so differs from taking single inputs.
# The input() function reads a single line of text from the user, so if multiple values are provided 
# separated by spaces, they are treated as a single string. This is why using split() is necessary to
# separate and process each individual input.

# Here's a quick breakdown of the process:

# Reading Input: The input() function reads a single line of text.

# Splitting the Input: The split() method divides the input string into individual components based 
# on spaces (or other delimiters).

# Processing Each Component: You then convert each component to the desired data type and store 
# it in a list.

# The map() function in Python is used to apply a given function to all items in an iterable (like a list) and return a map object (an iterator). This is particularly useful when you want to perform the same operation on all items in a list or other iterable.

# Syntax
# python
# map(function, iterable)
# function: The function to apply to each item.

# iterable: The iterable (such as a list) whose items will be passed to the function.

# Example Usage
# Here’s a simple example to illustrate the use of map():

# Convert a list of strings to integers:

# python
# # List of strings
# str_numbers = ["1", "2", "3", "4", "5"]

# # Use map() to convert each string to an integer
# int_numbers = list(map(int, str_numbers))

# print(int_numbers)  # Output: [1, 2, 3, 4, 5]
# Apply a function to each item:

# python
# # Define a function that squares a number
# def square(num):
#     return num * num

# # List of numbers
# numbers = [1, 2, 3, 4, 5]

# # Use map() to apply the square function to each item
# squared_numbers = list(map(square, numbers))

# print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
# Benefits of map()
# Efficiency: The map() function is generally more efficient than using a loop because it is implemented in C and optimized for performance.

# Readability: Using map() can make your code more concise and easier to read.

# Functional Programming: It allows you to apply functional programming principles by separating the operation (the function) from the data (the iterable).

# The map() function can be very powerful, especially when combined with other functional programming tools like filter() and reduce(). If you need more examples or have any specific questions about its usage, feel free to ask! 😊

