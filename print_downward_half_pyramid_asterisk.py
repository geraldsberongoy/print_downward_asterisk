# Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk)

for i in range(1, 6):
    for j in range(5, i-1, -1):
        print("*", end=" ")
    print("\r")