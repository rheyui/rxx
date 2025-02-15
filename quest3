c=['R','G', 'B', 'G', 'G', 'R', 'B', 'B', 'G']
dic={}
for v in c:
    if v not in dic:
        dic[v]=1
    else:
        dic[v]+=1
sorkey=sorted(dic.keys())
sorlist=[char for char in sorkey for _ in range(dic[char])]
print(sorlist)