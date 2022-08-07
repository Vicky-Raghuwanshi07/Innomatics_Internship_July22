import math

mean,sd=map(float,input().split())
x=input()
y1,y2=map(float,input().split())

def normalDistribution(x,mean,sd):
    return round(0.5 * (1 + math.erf((x - mean) / (sd * (2 ** 0.5)))),3)

print(normalDistribution(x,mean,sd))
print(normalDistribution(y2,mean,sd)-normalDistribution(y1,mean,sd))