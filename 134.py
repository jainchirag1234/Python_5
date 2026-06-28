search_str=input("Enter a string ")
with open("data.txt","r")as file:
    lines=file.readline()
matching_words=[]
for line in lines:
    words=line.strip().split()
    for word in words:
        if search_str.lower() in word.lower():
            matching_words.append(word)
with open("result.txt","w")as outfile:
    outfile.write("Words containing:\n".format(search_str))
    outfile.write("\n".join(matching_words))
print("Matching words written to 'result.txt'")
