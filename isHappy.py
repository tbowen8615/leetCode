def isHappy(n):
    seen = set()

    while n != 1:
        if n in seen:
            print("False")
            return False
        seen.add(n)

        n = sum(int(x) ** 2 for x in str(n))
    print("True")
    return True

isHappy(19)