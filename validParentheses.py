
def isValid(s):
    brackets = {')': '(', '}': '{', ']': '['}
    stack =[]

    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != brackets[char]:
                return False

    return len(stack) == 0