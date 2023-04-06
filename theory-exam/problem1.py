# 1. We can read 'abba' if we reverse the letters, it’s still 'abba', so this string is called palindrome. Write a python program to check if a string is palindrome or not. 

def check_palindrome(s):
    if s[-1::-1]==s:
        return True
    else:
        return False

result=check_palindrome('aba')
print(result)