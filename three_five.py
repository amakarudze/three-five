"""Program that prints numbers from 1 to 100. For multiples of 3, the program prints 'Three' instead of the number and
 for the multiples of 5 prints 'Five' instead. For multiples of both 3 and 5, the program prints 'ThreeFive'.

 Author: Anna Makarudze
 Contact: amakarudze@gmail.com"""

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("ThreeFive")
    if i % 3 == 0:
        print("Three")
    elif i % 5 == 0:
        print("Five")
    else:
        print(i)
