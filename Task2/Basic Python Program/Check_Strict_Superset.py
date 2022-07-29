a = set(map(int, input().split()))
n = int(input())
l=[]
for i in range(n):
    x = set(map(int, input().split()))
    if a.issuperset(x):
        if len(a)==len(x):
            l.append(False)
        else:
            l.append(True)
    else:
        l.append(a.issuperset(x))
print(all(l))
