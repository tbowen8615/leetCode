
def isPalindrome(s):
    new = ''
    for char in s:
        if char.isalnum():
            new += char.lower()

    return new == new[::-1]

print(isPalindrome("amanaplanacanalpanama"))