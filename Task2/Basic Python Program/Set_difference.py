# Enter your code here. Read input from STDIN. Print output to STDOUT
eng = int(input())
roll_eng = set(map(int,input().split()))
frnc = int(input())
roll_frnc = set(map(int,input().split()))

diffrce = roll_eng.difference(roll_frnc)

print(len(diffrce))
