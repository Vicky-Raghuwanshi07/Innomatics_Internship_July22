if __name__ == '__main__':
    s=[]
    for _ in range(int(input())):
        j,k=[],[]
        name = input()
        score = float(input())
        j.append(name)
        j.append(score)
        s.append(j) 
    # for i in range(0,len(s)):
    #     n.append(s[i][1])
    # n.sort()
    l = sorted(list(set([marks for name,marks in s])))
    for i in s:
        if i[1]==l[1]:
            k.append(i[0])
    k.sort()
    for i in k:
        print(i)
        