def check_pallindrome(str):
    
    clean_str = (str.replace(" ","")).lower()
    reverse_str = clean_str[::-1]
    return clean_str==reverse_str
str = input("Enter string")
if check_pallindrome(str):
    print("it is palindrome string")
else:
    print("It is not a pallindroma string")