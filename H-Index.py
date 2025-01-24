
def hIndex(citations):
    citations.sort(reverse=True)
    h_index = 0

    for i, citation in enumerate(citations, 1):
        if citation >= i:
            h_index = i
        else:
            break
    print(h_index)
    return h_index

citations = [0, 3, 6, 1, 5]
hIndex(citations)