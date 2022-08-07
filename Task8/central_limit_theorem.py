import math

def centralLimitTheorem(maxWeight,n,mean,sd):
    newMean=n*mean
    newSd=(n**0.5)*sd     
    return round(0.5 * (1 + math.erf((maxWeight - newMean) / (newSd * (2 ** 0.5)))),4)

if __name__=="__main__":
    maxWeight,n,mean,sd=input(),input(),input(),input()
    print(centralLimitTheorem(maxWeight,n,mean,sd))