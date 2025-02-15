def sorted(a):
    x=[]
    for v in a:
        x.append(abs(v)**2)
    x.sort()
    return x
le=[-12, -8 , -7, -5, 2, 4, 5, 11, 15]
sr=sorted(le)
print(sr)