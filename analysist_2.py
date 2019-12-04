data = []
count = 0
#读文件
with open("053 reviews.txt",'r') as f:
    for line in f:
        data.append(line)
        # count += 1
        # if count % 1000 == 0:
        #     print (len(data))

wc = {}
for d in data:
    words = d.split(' ')
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1

while True:
    word = input('please input your want to know the product:')
    if word == 'q':
        break
    if word in wc:
        print(word,wc[word])
    else:
        print('nothing')
print('Finshed')
