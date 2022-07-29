# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int,input().split())
arr = list(map(int,input().split()))
A = set(list(map(int,input().split())))
B = set(list(map(int,input().split())))
happieness=0
for n in arr:
    if n in A and n not in B:
        happieness +=1
    if n in B and n not in A:
        happieness -=1

print(happieness)
