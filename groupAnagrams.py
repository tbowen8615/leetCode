def groupAnagrams(strs):
    # 1. Create a dictionary to group strings by their sorted characters
    anagram_map = {}

    # 2. Process each string in the input list
    for s in strs:
        print(s)
        # Sort the characters of the string to create a key for anagrams
        # Using sorted() returns a list, join it to create a string key
        sorted_str = ''.join(sorted(s))
        print(sorted_str)

        # 3. Add the original string to the list for this sorted key
        # If key doesn't exist, create new list; otherwise append
        if sorted_str in anagram_map:
            anagram_map[sorted_str].append(s)
        else:
            anagram_map[sorted_str] = [s]
        print(anagram_map)

    # 4. Return list of all grouped anagrams (values from the dictionary)
    print(list(anagram_map.values()))
    return list(anagram_map.values())

strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)