#print numbers upto a particular digit using recurssion...

def printNosInRange(n1 , n2):
    if n1 > n2 :
        return 
    else :
        print(n1)
        return printNosInRange(n1+1 , n2)
        
printNosInRange(0,3)        
