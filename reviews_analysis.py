data = []
with open("053 reviews.txt",'r') as f:
    for line in f:
        data.append(line)
print (len(data))

