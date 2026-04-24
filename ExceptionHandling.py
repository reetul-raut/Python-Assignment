filename = input("Enter the filename to open: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile opened successfully!\n")
        print(content)

except FileNotFoundError:
    print("Error: The file does not exist.")

except PermissionError:
    print("Error: Permission denied. Cannot read the file.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")