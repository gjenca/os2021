
def log_call(f):

    def f_ret(arg):
        print('Volane {}({})'.format(f.__name__,arg)) 
        return f(arg)

    return f_ret

