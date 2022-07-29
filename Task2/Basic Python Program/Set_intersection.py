# Enter your code here. Read input from STDIN. Print output to STDOUT
eng = int(input())
roll_eng = set(map(int,input().split()))
frnc = int(input())
roll_frnc = set(map(int,input().split()))

intrsct = roll_eng.intersection(roll_frnc)

print(len(intrsct))
