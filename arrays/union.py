#finding union btw arrays by means of set
#better soln
def union(arr1,arr2):
    s = set()
    union = []
    
    for i in arr1:
        s.add(i)
    for j in arr2:
        s.add(j)
    for x in s:
        union.append(x)
        
    return union
    
arr1 = [1,3,4,2,3,3,3,5]    
arr2 = [3,4,5,6,6,7,8,9,8,9]

ans = union(arr1,arr2)
print(ans)

#-----------------------------------------------------------------------------------------------------------
#optimal - best soln for union
def union(arr1,arr2):
    i  = 0
    j = 0
    union = []
    arr1.sort()
    arr2.sort()
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            if len(union) ==0 or union[-1]!=arr1[i]:
                union.append(arr1[i])
            i+=1    
        else :
            if len(union) ==0 or union[-1]!=arr2[j]:
                union.append(arr2[j])
            j+=1
            
    while i < len(arr1):
        if union[-1]!=arr1[i]:
                union.append(arr1[i])
                i+=1
    while j < len(arr2)  :
        if  union[-1]!=arr2[j]:
                union.append(arr2[j])
                j+=1
    return union            
                
arr1 = [4,5,6,7,3,3,4,8,8]
arr2 = [1,1,2,3,4,5,5,9,1]
ans = union(arr1,arr2)
print(ans)
