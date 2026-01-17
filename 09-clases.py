class OperasBas:

    num1= 0
    num2=0
    res=0

    def __init__(self):
        self.num1=0
        self.num2=0

    def suma(self):
        self.res=self.num1+self.num1
        print("La suma es: {}" .format(self.res))

    def resta(self):
        self.res=self.num1+self.num2
        print("La resta es: {}" .format(self.res))

    
def main():
    obj= OperasBas()
    obj.suma()
    obj.resta()

if __name__ == "__main__":
    main()

        

    
    