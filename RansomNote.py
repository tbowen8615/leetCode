note = 'aa'
magazine = 'ab'

def ransomeNote(r, m):
    letter_count = {}
    for char in m:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

    for char in r:
        if char in letter_count and letter_count[char] > 0:
            letter_count[char] -= 1
        else:
            return False

    return True

ransomeNote(note, magazine)