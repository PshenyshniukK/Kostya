string = "This tool is cool. But that owl is awful. MAGIC TOOLS Ltd."

string1 = string.casefold().split()
print(string1)

for i in string1:
    if 'oo' in i:
        print(i, end=' ')