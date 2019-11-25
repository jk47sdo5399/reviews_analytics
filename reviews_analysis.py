data = []
count = 0
#读文件
with open("053 reviews.txt",'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print (len(data))
# print (len(data))

#每个留言的长度
sum_len = 0
for d in data:
    sum_len += len(d)
average_len = sum_len/len(data)
print(average_len)

#留言筛选
new = []
for d in data:
   if len(d) < 100:
       new.append(d)
print(len(new))

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print(len(good))

good = [d for d in data if 'good' in d]


