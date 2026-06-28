 # Q1: Create a file with user-input numbers and display contents

def write_numbers_to_file(filename):
    with open(filename, "w") as file:
        while True:
            num = int(input("Enter a number (0 to stop): "))
            if num == 0:
                break
            file.write(str(num) + "\n")

def read_file(filename):
    with open(filename, "r") as file:
        print("File Contents:")
        print(file.read())

filename = "numbers.txt"
write_numbers_to_file(filename)
read_file(filename)
