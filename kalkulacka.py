class Kalkulacka:
    def vydel(self, a,b):
        if b==0:
            raise Exception("Nelze delit nulou")
        return a/b