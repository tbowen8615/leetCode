str1 = "tyler"
str2 = "bowen"

for x, y in zip(str1, str2):
    print(x, y)

for x, y in zip(str1, str2):
    if x != y:
        print("this pair is different")
    else:
        print("this pair is the same")

hash_map = zip(str1, str2)

print(list(hash_map))