def isPalindrome(s):
    # Initialize two pointers: left at the start, right at the end
    left = 0
    right = len(s) - 1

    # While left is less than right
    while left < right:
        # Move left pointer if the character is not alphanumeric
        while left < right and not s[left].isalnum():
            left += 1
        # Move right pointer if the character is not alphanumeric
        while left < right and not s[right].isalnum():
            right -= 1
        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

    return True


# Test cases
print(isPalindrome("A man, a plan, a canal: Panama"))  # Output: True
print(isPalindrome("race a car"))  # Output: False
print(isPalindrome(""))  # Output: True