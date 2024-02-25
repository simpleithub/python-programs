#a string is a palindrome or not by recursion

def palindrome(word) :
    if len(word) == 1 :
        return True
    elif word[0] == word[-1]:
        word = word[1:]
        palindrome(word)
        return True
    else:
        return False
        
x = input("enter a word to find if its a palindrome or not : ") 
if palindrome(x) == True :
    print(x ,"is palindrome")
else :
    print(x ,"is not a palindrome")
