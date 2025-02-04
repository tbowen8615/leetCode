def destCity(paths):
    # Collect all destination cities
    destSet = set()
    for start, end in paths:
        destSet.add(end)

    # Remove any city that also appears as a start
    for start, end in paths:
        if start in destSet:
            destSet.remove(start)

    return destSet.pop()