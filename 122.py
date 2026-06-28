def write_numbers_to_file(filename):
    with open(filename,"w") as file:
        while True:
            num=int(input("Enter a number"))
            if num == 0:
                break
            file.write(str(num)+"\n")
def read_file(filename):
    with open(filename,"r") as file:
        print("File Contents:")
        print(file.read())
filename="numbers.txt"
write_numbers_to_file(filename)
read_file(filename)
