# rotating element to right with 1 step
#SOLUTION-1
def right_rotate(arr):
    arr.sort()
    temp = arr[0]
    for i in range(1,len(arr)):
        arr[i-1] = arr[i]
        
    arr[-1] = temp
    return arr
    
  
arr = [1,2,3,4,5]

print(right_rotate(arr))

