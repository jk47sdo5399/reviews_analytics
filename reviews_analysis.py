data = []
count = 0
with open("053 reviews.txt",'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print (len(data))
# print (len(data))

sum_len = 0
for d in data:
    sum_len += len(d)
average_len = sum_len/len(data)
print(average_len)


