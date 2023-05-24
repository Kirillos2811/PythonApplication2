left_border = int(input("left border = "))
right_border = int(input("right border = "))

res = {}
for i in range(left_border, right_border + 1):
    res[i] = i**i

print(res)