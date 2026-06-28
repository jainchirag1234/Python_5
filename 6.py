# Function to write user input strings to a file
def write_strings_to_file(filename):
    with open(filename, "w") as file:
        print("Enter strings (one per line). Type 'STOP' to finish:")
        while True:
            value = input()
            if value.upper() == "STOP":
                break
            file.write(value + "\n")

# Function to read file and count string occurrences
def count_string_frequencies(filename):
    freq_dict = {}
    with open(filename, "r") as file:
        for line in file:
            word = line.strip()
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1
    return freq_dict

# File name
filename = "strings.txt"

# Execute functions
write_strings_to_file(filename)
frequencies = count_string_frequencies(filename)

# Display output
print("\nString Frequency Dictionary:")
print(frequencies)
N
