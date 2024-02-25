#sum of N numbers using recursion...
def sumOfNos(n , sum=0):
    #base case
    if n == 0:
        return sum
    else :
        sum += n
        return sumOfNos(n-1 , sum)

x = int(input("enter number : "))        
ans = sumOfNos(x)
print("the sum of numbers from 1 to ",x," is ",ans)
