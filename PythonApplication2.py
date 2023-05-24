set1 = set(input().split(" "))
set2 = set(input().split(" "))

count = 0
for el in set1:
    if el in set2:
        count += 1

print(count)