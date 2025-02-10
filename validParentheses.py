
def isValid(s):
    # Create a dictionary for matching closing brackets (keys) with corresponding open brackets (values)
    brackets = {')': '(', '}': '{', ']': '['}
    # initialize empty stack to keep track of unmatched opening brackets
    stack = []
    # iterate through the string
    for char in s:
    # if the character is an open bracket, push it onto the stack
        if char in '({[':
            stack.append(char)
            print(stack)
    # else if the character is a closing bracket, 1) check if the stack is empty.
    # 2) pop the stack and verify if the popped element matches the expected opening bracket from
    # the dictionary
        elif char in ')}]':
            if not stack or stack.pop() != brackets[char]:
                print("Invalid string")
                return False
    # After processing all characters, check if the stack is empty.
    if len(stack) != 0:
        print("Invalid string")
        return False
    else:
        print("Valid string")
    return True

s = '({[]})'
isValid(s)