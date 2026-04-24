s = "baba"
mid = len(s)//2
p = list(s)
if len(s)%2 == 0:
    for i in range(mid,0,1):
        for j in range(mid,len(s), 1):
            if p[i] == p[j]:
                continue
            else:
                p.remove(i)
                p.remove(j)
    p = str(p)
else:
