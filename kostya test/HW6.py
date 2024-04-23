# Heigth = int(input("Heigth : "))
# Width = int(input("Width : "))
# for i in range(Width):
#     if i == 0 or i == Width - 1:
#         for j in range(Heigth):
#             print("* ", end="")
#         print()
#     else:
#         for j in range(Heigth):
#             if j == 0 or j == Heigth - 1:
#                 print("* ", end="")
#             else:
#                 print(end="  ")
#         print()


Heigth = int(input("Height : "))
Width = int(input("Width : "))

for i in range(Heigth):
    if (i == 0) or (i == Heigth - 1): # Checking if it is first or last row
        print('* ' * Width)
    else:
        print('* ' + '  ' *(Width - 2) + '*')