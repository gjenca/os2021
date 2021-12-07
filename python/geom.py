
class Obdlznik:
    
    def __init__(self,a,b):

        self.a=a
        self.b=b

    def plocha(self):

        return self.a*self.b

    def __repr__(self):

        return 'Obdlznik(%s,%s)' % (self.a,self.b)

    def __bool__(self):

        return self.a!=0 and self.b!=0



