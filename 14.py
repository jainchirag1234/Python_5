nums=[10,12,45,10,12,45,10,12,90,10,12,10,10]

k=int(input("Enter the value of k"))
freq_dict={}
for num in nums:
    if num in freq_dict:
        freq_dict[num]+=1
    else:
        freq_dict[num]=1
sorted_freq=sorted(freq_dict.items(),key=lambda x:x[1],reverse=True)
print(f"Top {k} most frequent elements are:")
for i in range(min(k,len(sorted_freq))):
    print(sorted_freq[i][0])
