# Enter your code here. Read input from STDIN. Print output to STDOUT
num =int(input())
s = set({})
for i in range(num):
    coun = str(input().split())
    s.add(coun)
    
    
print(len(s))   
