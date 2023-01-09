import add
import subtract
import Modulus
import SquareRoot
a = int (input ("Input first number: "))
b= int (input ("Input second number: "))
sum = add.add(a,b)
print (sum)
subtract = subtract.subtract(a,b)
print (subtract)
c=Modulus.Modulus(a,b)
print(c)
c= SquareRoot.SquareRoot(a)
print(c)
