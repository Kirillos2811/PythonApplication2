n = int(input())
arr = list(map(int, input().split(" ")))

last_element = arr.pop()
arr.insert(0, last_element)
print(*arr)