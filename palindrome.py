def isPalindrome(word):
    if word==word[::-1]:
        return True
    else:
        return False
a=input("word please")
b=str(isPalindrome(a))
print("Palinedrome?" +b)