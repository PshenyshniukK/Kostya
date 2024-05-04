
string1 = input().lower().lstrip().rstrip()
str2 = int(len(string1))
result = ''
for i in range(str2 - 1, -1, -1):
    result += string1[i]
result2 = result
print(string1)
print(result)
print(result2)
print(string1 == result2)
