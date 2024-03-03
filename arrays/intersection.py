#brute-force method not an optimal soln
def intersection(arr1,arr2):
    inter_map = []
    for i in arr1 :
        for j in arr2 :
            if i == j :
                if i not in inter_map :
                    inter_map.append(i)
    return inter_map
    
arr1 = [1,2,3,1,2,3,1,4,5]
arr2 = [1,6,7,7,7,8,6,9,2]
ans = intersection(arr1,arr2)
print(ans)                

#optimal method for intersection of arrays is to use set and union operator
def intersection(arr1,arr2):
    final = set(arr1) & set(arr2)
    return final
    
arr1 = [1,2,3,1,2,3,1,4,5]
arr2 = [1,6,7,7,7,8,6,9]
ans = intersection(arr1,arr2)
print(ans)
