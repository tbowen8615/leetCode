
def isPalindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())

    # Use two pointers to check if it's a palindrome
    left = 0
    right = len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            print("False")
            return False
        left += 1
        right -= 1

    print("True")
    return True

s = "A man, a plan, a canal: Panama"
isPalindrome(s)