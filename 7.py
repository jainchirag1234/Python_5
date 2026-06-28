# Function to write multiple lines to a text file
def write_text_to_file(filename):
    with open(filename, "w") as file:
        print("Enter multiple lines of text. Type 'STOP' on a new line to finish:")
        while True:
            line = input()
            if line.upper() == "STOP":
                break
            file.write(line + "\n")

# Function to search for a word in the file and count occurrences
def search_word_in_file(filename, search_word):
    with open(filename, "r") as file:
        print(f"\nLines containing the word '{search_word}':\n")
        for line in file:
            words = line.strip().split()
            word_count = words.count(search_word)
            if word_count > 0:
                print(f"Line: {line.strip()}  | Frequency: {word_count}")

# File name
filename = "textfile.txt"

# Execute functions
write_text_to_file(filename)

# User input for word to search
search_word = input("\nEnter a word to search in the file: ")
search_word_in_file(filename, search_word)
