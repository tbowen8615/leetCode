def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for char_s, char_t in zip(s, t):
        if char_s in s_to_t:
            if s_to_t[char_s] != char_t:
                print("False")
                return False
        elif char_t in t_to_s:
            if t_to_s[char_t] != char_s:
                print("False")
                return False
        else:
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s
    print("True")
    return True

str1 = 'egg'
str2 = 'adh'

isIsomorphic(str1, str2)