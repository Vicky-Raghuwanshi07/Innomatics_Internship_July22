def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
def nCr(n,r):
    return factorial(n)/(factorial(r) * factorial(n-r))

if __name__=='__main__':
    p,n=map(float,input().split())
    p/=100
    q=1-p
    firstSum=0
    for i in range(0,3):
        ncr=nCr(n,i)
        temp=(p**i) * (q** (n-i))
        firstSum+=ncr*temp
        
    print(round(firstSum,3))

    secondSum=0
    for i in range(2,11):
        ncr=nCr(n,i)
        temp=(p**i) * (q** (n-i))
        secondSum+=ncr*temp

    print(round(secondSum,3))



