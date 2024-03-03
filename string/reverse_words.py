#reverse the string by means of words separated by '.'
def reverseWords(S):
        # code here 
    x = S.split(".")
    x.reverse()
    y = ".".join(x)
    return y
    
S = "sai.geetha.hello"   
print(reverseWords(S))
