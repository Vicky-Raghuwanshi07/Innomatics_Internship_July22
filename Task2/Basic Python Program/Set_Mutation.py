n = int(input())
s = set(map(int, input().split()))
m = int(input())
for i in range(m):
    con = input().split()
    s1 = set(map(int, input().split()))
    if con[0]=='intersection_update':
        s.intersection_update(s1)
        con,s1=0,0
        continue
    elif con[0]=='update':
        s.update(s1)
        con,s1=0,0
        continue
    elif con[0]=='symmetric_difference_update':
        s.symmetric_difference_update(s1)
        con,s1=0,0
        continue
    elif con[0]=='difference_update':
        s.difference_update(s1)
        con,s1=0,0
        continue
print(sum(s))
