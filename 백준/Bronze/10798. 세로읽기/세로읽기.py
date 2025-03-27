resultlist = [ [] for _ in range(15)]
result = ""
for i in range(5):
    word = list(input())
    count = 0
    for j in word:
        resultlist[count].append(j)
        count += 1
        

for i in resultlist:
    result += ''.join(i)

print(result)