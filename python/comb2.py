
from functools import cache

@cache
def comb(n,k):

    if n==k or k==0:
        return 1
    return comb(n-1,k-1)+comb(n-1,k)

