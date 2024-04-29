
string1 = input()
str2 = int(len(string1))
result = ''
for i in range(str2 -1, -1, -1):
    if i == i:
        result += string1[i]

string1 = string1.replace(' ', '')
string1 = string1.lower()
result = result.replace(' ', '')
result = result.lower()
print(string1)
print(result)

print(string1 == result)