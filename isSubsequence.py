s = "abc"
t = "ahbgdc"

def isSubsequence(s,t):
    i = 0
    j = 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)

print(isSubsequence(s, t))