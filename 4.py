# Function to take user input and store mixed data in a file
def write_mixed_data_to_file(filename):
    with open(filename, "w") as file:
        print("Enter elements (integer, float, or string). Type 'STOP' to finish:")
        while True:
            value = input()
            if value.upper() == "STOP":
                break
            file.write(value + "\n")

# Function to read data from file and split into separate files based on data type
def split_data(input_file, int_file, float_file, str_file):
    with open(input_file, "r") as file, \
         open(int_file, "w") as int_f, \
         open(float_file, "w") as float_f, \
         open(str_file, "w") as str_f:

        for line in file:
            value = line.strip()
            try:
                # Try converting to integer
                num = int(value)
                int_f.write(value + "\n")
            except ValueError:
                try:
                    # Try converting to float
                    num = float(value)
                    float_f.write(value + "\n")
                except ValueError:
                    # If conversion fails, it's a string
                    str_f.write(value + "\n")

# File names
input_filename = "mixed_data.txt"
int_filename = "integers.txt"
float_filename = "floats.txt"
str_filename = "strings.txt"

# Execute the functions
write_mixed_data_to_file(input_filename)
split_data(input_filename, int_filename, float_filename, str_filename)

print(f"Data has been successfully split into '{int_filename}', '{float_filename}', and '{str_filename}'.")
