# Enter your code here. Read input from STDIN. Print output to STDOUT
eng = int(input())
roll_eng = set(map(int,input().split()))
frc = int(input())
roll_frc = set(map(int,input().split()))

un = roll_eng.union(roll_frc)

print(len(un))
