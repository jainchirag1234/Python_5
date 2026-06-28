# Function to take user input and store numbers in a file
def write_numbers_to_file(filename):
    with open(filename, "w") as file:
        print("Enter numbers (0 to stop):")
        while True:
            num = int(input())
            if num == 0:
                break
            file.write(str(num) + "\n")

# Function to read numbers from a file and separate them into odd and even files
def split_numbers(input_file, odd_file, even_file):
    with open(input_file, "r") as file, open(odd_file, "w") as odd, open(even_file, "w") as even:
        for line in file:
            num = int(line.strip())
            if num % 2 == 0:
                even.write(line)  # Write even numbers to even_file
            else:
                odd.write(line)   # Write odd numbers to odd_file

# File names
input_filename = "numbers.txt"
odd_filename = "odd_numbers.txt"
even_filename = "even_numbers.txt"

# Execute the functions
write_numbers_to_file(input_filename)
split_numbers(input_filename, odd_filename, even_filename)

print(f"Numbers have been successfully split into '{odd_filename}' and '{even_filename}'.")
