#print name for a particular no.of.times by recurssion

def printNameNtimes(name,n,c=0): 
    if c >= n :
        return 
    else :
        print(name)
        c+=1
        return printNameNtimes(name , n ,c)

x = input("enter ur name :")
n = int(input("enter count :"))
printNameNtimes(x,n)       
