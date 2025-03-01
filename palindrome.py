def isPalindrome(word):
    for i in range(len(word)):
        if word[i]==word[len(word)-1-i]:
            return True
        else: 
            return False

a=input("word please")
b=str(isPalindrome(a))
print("Palindrome?" +b)

