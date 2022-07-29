n = int(input())
s = set(map(int, input().split()))
cmd = int(input())
for i in range(cmd):
    
    c=input().split()
    if c[0]=="remove":
        s.remove(int(c[1]))
    elif c[0]=="discard":
        s.discard(int(c[1]))
    else:
        s.pop()
print(sum(list(s)))
