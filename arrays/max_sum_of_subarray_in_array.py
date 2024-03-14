# to find the maximum sum in a sub array ::::
def maxSubarraySum(arr):
    maxi = 0  # maximum sum
    sum = 0
    n =len(arr)
    for i in range(n):
        sum +=arr[i]
        
        if sum > maxi :
            maxi = sum
        if sum < 0:
            sum = 0
    return maxi

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubarraySum(arr))
