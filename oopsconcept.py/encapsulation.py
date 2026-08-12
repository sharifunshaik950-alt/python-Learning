class encap:

    __a=10
    def setA (self,b):
      self.__a=self.__a+b
    def getA(self):
        return self.__a 
e=encap()
e.setA(30)
print(e.getA())       