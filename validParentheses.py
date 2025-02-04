
def isValid(s):
    brackets = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in '({[':
            stack.append(char)
            print(stack)
        elif char in ')}]':
            if not stack or stack.pop() != brackets[char]:
                print("Invalid string")
                return False
    if len(stack) != 0:
        print("Invalid string")
        return False
    else:
        print("Valid string")
    return True

s = '({[]})'
isValid(s)