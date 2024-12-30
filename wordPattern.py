def wordPattern(pattern, s):
    pattern_to_s = {}
    s_to_pattern = {}
    s = s.split()
    if len(pattern) != len(s):
        print("False")
        return False


    for letter, word in zip(pattern, s):
        if letter in pattern_to_s:
            if pattern_to_s[letter] != word:
                print("False")
                return False
        elif word in s_to_pattern:
            if s_to_pattern[word] != letter:
                print("False")
                return False
        else:
            pattern_to_s[letter] = word
            s_to_pattern[word] = letter

    print("True")
    return True


pattern = "abcde"
string = "Hello world how are are"
wordPattern(pattern, string)