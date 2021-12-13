
def memoize(f):

    d={}
    
    def f_ret(*args):
        if args in d:
            return d[args]
        else:
            d[args]=f(*args)
            return d[args]
    return f_ret

