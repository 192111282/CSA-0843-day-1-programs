n=[1,2,3,4,5]
def sumsquare(n):
    odd=0
    even=0
    for i in n:
        if i%2==0:
            even =even + i**2
        else:
            odd = odd + i**2
    n=[odd, even]
    return(n)
print (sumsquare(n))
