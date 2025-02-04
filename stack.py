
stack =[]
delimmiters = {')':'(', '}':'{', ']':'['}
s = "({[]})("

for i in s:
    if i in "({[":
        stack.append(delimmiters[i])
        print(stack)

for i in s:
    if i in ")}]" and stack[-1] == delimmiters[i]:
        stack.pop()

print(stack)
