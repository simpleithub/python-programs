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

