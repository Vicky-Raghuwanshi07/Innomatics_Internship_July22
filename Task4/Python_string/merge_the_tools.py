def merge_the_tools(string, k):
    k=int(k)
    s = (len(string)//int(k))
    f,j=0,int(k)
    for i in range(s):
        l = []
        for c in string[f:k]:
            if c in l:
                continue
            else:
                l.append(c)
        print(''.join(l))
        f,k=k,k+j
    
