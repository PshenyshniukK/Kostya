
string1 = input().lower().replace(' ', '')
str2 = int(len(string1))
result = ''
for i in range(str2 -1, -1, -1):
    if i == i:
        result += string1[i]

print(string1)
print(result)

print(string1 == result)