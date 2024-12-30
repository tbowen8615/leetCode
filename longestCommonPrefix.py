def longestCommonPrefix(strs):

    if not strs:
        return ""

    lcp = strs[0]
    for str in strs[1:]:
        while not str.startswith(lcp):
            lcp = lcp[:-1]
        if not lcp:
            return ""
    print(lcp)
    return lcp

strs = ["flower", "flow", "flight"]
longestCommonPrefix(strs)