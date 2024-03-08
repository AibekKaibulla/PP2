# Write a Python program with builtin function that checks whether a passed string is palindrome or not.

def isPalindrome(s):
    cleaned_s = s.replace(" ", "").lower()

    return cleaned_s == ''.join(reversed(cleaned_s))


string = input()

if isPalindrome(string):
    print("It's a Palindrome!")
else:
    print("OPPPS, it's not a palindrome :( ")