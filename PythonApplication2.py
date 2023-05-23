string = list(input())
res_string = ""
previous_char = ""
for i in reversed(range(len(string))):
    if string[i] == " " and previous_char == " ":
        string.pop(i)
    previous_char = string[i]

print("".join(string))
