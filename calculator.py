class calculator:
    def __init__(self):
        pass
    def add(self,x,y):
        return x+y
    def subtract(self,x,y):
        return x-y
    def multiply(self,x,y):
        return x*y
    def divide(self,x,y):
        if y!=0:
            return x/y
        print("Divide by zero")

calc=calculator()
print('\t'*50,'CALCULATOR','\t'*50)  
print('\t'*50,'1- ADD','\t'*50)
print('\t'*50,'2- SUBTRACT','\t'*50)
print('\t'*50,'3- MULTIPLY','\t'*50)
print('\t'*50,'4- DIVIDE','\t'*50)

try:
    i = int (input('Operation:  '))
    x,y=map(int,input('Two Values are : ').split())
    ch ='again'
    while ch=='again' and i in {1,2,3,4}:
        if i ==1:
            print(calc.add(x,y))
        elif i==2:
            print(calc.subtract(x,y))
        elif i==3:
            print(calc.multiply(x,y))
        elif i==4:
            print(calc.divide(x,y))
        
        print("Press Y if u wish to calculate again")
        ch=input()
    else:
        print("INPUT OUT OF RANGE")
except:
    print("PASS THE INPUT CORRECTLY")
finally:
    print('\t'*50,"END",'\t'*50)
    