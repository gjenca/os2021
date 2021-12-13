
class Obdlznik:

    def __init__(self,a,b):
        
        self.a=a
        self.b=b

    def obvod(self):

        return 2*(self.a+self.b)

    def plocha(self):

        return self.a*self.b

    def expand(self,coef):

        self.a=self.a*coef
        self.b=self.b*coef


class Stvorec(Obdlznik):

    def __init__(self,x):

        self.a=x
        self.b=x

