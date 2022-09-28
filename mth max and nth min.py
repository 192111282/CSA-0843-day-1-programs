number=int(input("Enter the Number of digits: "))
arr=[]
for i in range (number):
    a=int(input("Enter the Number: "))
    arr.append(a)
temp=0
for i in range (0, len (arr)):
    for j in range (i+1, len(arr)):
        if (arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
rarr=arr[::-1]
m=int(input("m="))
n=int(input("n="))
print("%d max number is %d"%(m,rarr[m-1]))
print("%d min number is %d"%(n,arr[n-1]))
sum=rarr[m-1]+arr[n-1]
difference=rarr[m-1]-arr[n-1]
print("sum=",sum)
print("Difference=",difference)
