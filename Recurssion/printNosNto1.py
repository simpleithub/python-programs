#print numbers from N to 1 using recursion>...
def printNumsNto1(n , c=None):
    #base case
    if c == None :
        c =n 
    if c == 0:
        return 
    else :
        print(c)
        c -=1
        return printNumsNto1(n , c)

x = int(input("enter number : ")) 
printNumsNto1(x)
