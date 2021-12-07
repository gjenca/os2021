#!/usr/bin/env python3
'''Popis modulu prvočisla
'''
import math

def prvocisla(n,s=2):
    '''Vráti zoznam prvočísiel od s po n.
Predvolená hodnota s je 2.'''

    ret=[]
    for k in range(s,n):
        for d in range(2,int(math.sqrt(k))+1):
            if (k % d)==0:
                break
        else:
            ret.append(k)
    return ret


