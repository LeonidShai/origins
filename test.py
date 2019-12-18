print("AAAAAAaaaaaaa")

pr = {2: [2, 3], 1: [1, 5, 8], 3: [4, 1]}
s = 0
for key in pr.keys():
    s += len(pr[key])

print(pr, s)
l = []
for key in pr.keys():
    l.append(key)
l.sort()
print(pr, l)

a = []
for i in l:
    for j in pr[i]:
        a.append(j)
print(a)
print(a[2])