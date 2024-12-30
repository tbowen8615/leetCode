def validAnagram(s, t):

    frequency_counter = {}

    for i in s:
        if i in frequency_counter:
            frequency_counter[i] += 1
        else:
            frequency_counter[i] = 1

    for i in t:
        if i in frequency_counter:
            frequency_counter[i] -= 1
            if frequency_counter[i] < 0:
                print("False")
                return False
        else:
            print("False")
            return False
    print("True")
    return True

s = "anagram"
t = "nagaram"

validAnagram(s, t)