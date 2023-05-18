print("Введите слово из маленьких латинских букв")
word = input()
a = 0
e = 0
i = 0
o = 0
u = 0
consonants = 0
for letter in word:
    if letter == "a":
        a += 1
    elif letter == "e":
        e += 1
    elif letter == "i":
        i += 1
    elif letter == "o":
        o += 1
    elif letter == "u":
        u += 1
    else:
        consonants += 1

print("В слове", a + e + i + o + u, "гласных букв")
print("В слове", consonants, "согласных букв")

print("Буква 'a':", end = " ")
if a > 0:
    print(a)
else:
    print(False)

print("Буква 'е':", end = " ")
if e > 0:
    print(e)
else:
    print(False)

print("Буква 'i':", end = " ")
if i > 0:
    print(i)
else:
    print(False)

print("Буква 'o':", end = " ")
if o > 0:
    print(o)
else:
    print(False)

print("Буква 'u':", end = " ")
if u > 0:
    print(u)
else:
    print(False)