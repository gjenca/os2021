#!/usr/bin/env python3
import math

x=10

# Zoznam prvocisel <= n
def prvocisla(n,s=2):

    ret=[]
    for k in range(s,n):
        for d in range(2,int(math.sqrt(k))+1):
            if (k % d)==0:
                break
        else:
            ret.append(k)
    return ret


            
#print(prvocisla(100,50))

