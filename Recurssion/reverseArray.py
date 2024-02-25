 #reverse an array

def reverseArray(arr, first=None, last=None):
    if first == None and last == None:
        first = 0
        last = len(arr) - 1
    
    if first >= last:
        return
    else:
        arr[first], arr[last] = arr[last], arr[first] 
        reverseArray(arr, first + 1, last - 1)

arr = [1, 2, 3]
x = reverseArray(arr)
print(arr)
