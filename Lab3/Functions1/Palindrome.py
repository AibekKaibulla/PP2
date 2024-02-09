def is_palindrome(input_string):
    reversed_string = input_string[::-1]
    if reversed_string == input_string:
        print(True)
    else:
        print(False)

phrase = input("Enter a string: ")
is_palindrome(phrase)
