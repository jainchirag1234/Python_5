# Function to write student records to a file
def write_student_records(filename):
    with open(filename, "w") as file:
        print("Enter student records in the format: RollNo, Mark1, Mark2, Mark3")
        print("Type 'STOP' to finish.")
        
        while True:
            record = input()
            if record.upper() == "STOP":
                break
            file.write(record + "\n")

# Function to read student records from file and display formatted mark list
def display_mark_list(filename):
    print("\nMark List:")
    print(f"{'Roll No.':<10}{'Mark-1':<10}{'Mark-2':<10}{'Mark-3':<10}{'Total':<10}")
    print("-" * 50)

    with open(filename, "r") as file:
        for line in file:
            data = line.strip().split(",")
            roll_no = data[0]
            marks = list(map(int, data[1:]))  # Convert marks to integers
            total_marks = sum(marks)
            print(f"{roll_no:<10}{marks[0]:<10}{marks[1]:<10}{marks[2]:<10}{total_marks:<10}")

# File name
filename = "student_records.txt"

# Execute the functions
write_student_records(filename)
display_mark_list(filename)
