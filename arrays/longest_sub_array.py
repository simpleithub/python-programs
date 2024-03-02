#finding longeest sub array for the given sum!!
def longest_subarray(arr,s):
    x = len(arr)
    maxi = 0
    for i in range(0,x):
        add = 0
        for j in range(i,x):
            add+=arr[j]
            
            if add == s:
                maxi = max(maxi,j-i+1)
                #end(j)-start(i)+1 ;;;adding 1 is becoz its in index,we need number ie length of sub array ....
    return maxi
    
    
arr=[3,2,1,4,1,2,2]
s = 5
ans = longest_subarray(arr,s)
print(ans)
            
