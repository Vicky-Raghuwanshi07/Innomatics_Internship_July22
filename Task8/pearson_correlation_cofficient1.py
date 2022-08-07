def mean(x):
    return round(sum(x)/float(n),1)

def standardDeviation(values,mean):
    data=[(val-mean)**2 for val in values]
    return (sum(data)/float(len(data)))**0.5


def pearsonCorrelationCoefficient(x,y):
    xMean=mean(x)
    yMean=mean(y)
    xStd=standardDeviation(x,xMean)
    yStd=standardDeviation(y,yMean)
    numerator = sum( (x[i]-xMean)*(y[i]-yMean) for i in range(n))
    denominator = n*xStd*yStd
    return round((numerator/denominator),3)

if __name__=="__main__":
    n=input()
    x=map(float,input().split())
    y=map(float,input().split())
    print(pearsonCorrelationCoefficient(x,y))