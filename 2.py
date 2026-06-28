# Q2: Create a text file with multiple lines and display details

def write_text_file(filename):
    with open(filename, "w") as file:
        print("Enter multiple lines (type 'STOP' to finish):")
        while True:
            line = input()
            if line.strip().upper() == "STOP":
                break
            file.write(line + "\n")

def display_file_contents(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        print("\nEntire Text File:")
        print("".join(lines))

        print("\nNumber of lines:", len(lines))

        n = int(input("\nEnter line number to start displaying from: "))
        print("\nLines from line", n, "onwards:")
        print("".join(lines[n-1:]))

        print("\nWord count in each line:")
        for i, line in enumerate(lines, 1):
            print(f"Line {i}: {len(line.split())} words")

filename = "textfile.txt"
write_text_file(filename)
display_file_contents(filename)
