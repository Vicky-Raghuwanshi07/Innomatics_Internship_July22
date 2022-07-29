# Enter your code here. Read input from STDIN. Print output to STDOUT
ts_case = int(input())
for i in range(ts_case):
    set1_no = int(input())
    s1 = set(map(int,input().split()))
    set2_no = int(input())
    s2 = set(map(int,input().split()))
    print(s1.issubset(s2))
