eng = int(input())
roll_eng = set(map(int,input().split()))
frnc = int(input())
roll_frnc = set(map(int,input().split()))

sy_diff = roll_eng.symmetric_difference(roll_frnc)

print(len(sy_diff))
