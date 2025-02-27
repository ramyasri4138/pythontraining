import os

filename = "example.txt"

# 1. Writing to a File
with open(filename, "w") as file:
    file.write("Hello, this is a sample text file.\n")
    file.write("Python makes file handling easy!\n")
print("File written successfully.")

# 2. Checking if the File Exists
if os.path.exists(filename):
    print(f"File '{filename}' exists!")

# 3. Reading the Entire File
with open(filename, "r") as file:
    content = file.read()
print("\nFile Content:\n", content)

# 4. Appending to the File
with open(filename, "a") as file:
    file.write("This is a new line appended to the file.\n")
print("File appended successfully.")

# 5. Reading the File Line by Line
print("\nReading File Line by Line:")
with open(filename, "r") as file:
    for line in file:
        print(line.strip())  # Removes extra newline characters