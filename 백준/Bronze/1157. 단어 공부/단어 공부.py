dic = {}
word = input()
lowerword = word.lower()

for i in lowerword:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

count = len([key for key, value in dic.items() if value == dic[max(dic, key = dic.get)]])

if count > 1:
    print('?')
else:
    print(max(dic, key = dic.get).upper())