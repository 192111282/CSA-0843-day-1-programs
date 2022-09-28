rows = int(input("Enter number of rows: "))
coe = 1
for i in range(1, rows+1):
    for space in range(1,rows-i+1):
        print(" ",end="")
    for j in range(0, i):
        if j==0 or i==0:
            coef = 1
        else:
            coe = coe * (i - j)//j
        print(coe, end =" ")
    print()
