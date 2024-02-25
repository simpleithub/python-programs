#factorial of n by recursion...
def factorialOfN(n) :
    if n == 0 :
        return 1
    else :
        return n*factorialOfN(n-1)
x = int(input("enter a number :"))    
print("the factorial of",x,"is ",factorialOfN(x))       

