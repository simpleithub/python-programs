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


#SOLUTION-2
#right rotate optimal method for multiple steps
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
  

def rotate_array(arr,d) :
    n = len(arr)
    d = d % n
    reverse(arr,0,n-1)
    reverse(arr,d,n-1)
    reverse(arr,0,d-1)
    
    
arr = [1,2,3,4,5,6,7]    
d = 1
rotate_array(arr,d)
print(arr)
