def reverse_number(int):  
    int1 = ""
    for i in int:  
        int1 = i + int1  
    return int1
int = input("enter the number : ")
print("The original string is: ",int)  
print("The reverse string is",reverse_number(int))
