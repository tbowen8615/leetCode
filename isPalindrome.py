
def isPalindrome(s):
    # Set all characters to lowercase, remove non-alphanumeric characters, and join them together
    cleaned = ''.join(char.lower() for char in s if char.isalnum())

    # Initialize two pointers one at the beginning of the string and one at the end
    left = 0
    right = len(cleaned) - 1

    # while the left pointer is less than the right, check if the characters they point to are the same
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