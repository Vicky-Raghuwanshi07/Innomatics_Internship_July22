def average(array):
    # your code goes here
    a = set(array)
    sum = 0
    for i in a:
        sum+=i
    avg = sum/len(a)
    return avg
        
