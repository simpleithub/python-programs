
#to find the arrays are equal or  not
def arrayEqualChk(A,B,N):
        
        if len(A) != len(B):
            return False
        
        A.sort()
        B.sort()
        
        for i in range (0,N):
            if A[i] != B[i]:
                return False
        return True

A = [2,6,4,2]
B = [2,6,2,4]
N = 4
if check(A,B,N) == True :
    print("arrays are equal") 
else :
    print("arrays are not equal")
    
