# Writing to a file (creates file if it doesn't exist)
file = open("sample.txt", "w")
file.write("Hello, this is the first line.\n")
file.write("File handling in Python is easy.\n")
file.close()   # Properly close the file

# Reading from the file
file = open("sample.txt", "r")
content = file.read()
print("File contents after writing:")
print(content)
file.close()

# Appending to the file
file = open("sample.txt", "a")
file.write("This line is added later.\n")
file.close()

# Reading again after appending
file = open("sample.txt", "r")
content = file.read()
print("File contents after appending:")
print(content)
file.close()