# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
num1 = set(map(int,input().split()))
n = int(input())
num2 = set(map(int,input().split()))
diff1 = num1.difference(num2)
diff2 = num2.difference(num1)

un = diff1.union(diff2)

for i in sorted(list(un)):
    print(i)
