li = set()
li2 = set()
a,b = map(int, input().split(" "))

for i in range(a):
    w = input()
    li.add(w)

for j in range(b):
    w = input()
    li2.add(w)

re = sorted(li & li2)

print(len(re))

for k in re:
    print(k)