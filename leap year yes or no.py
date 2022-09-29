def Leap(year):
         if(year % 400 == 0):
            return True
         else:
             return False
year = int(input("Enter a valid year :"))
if(Leap(year)):
    print("Leap Year")
else:
    print("Not a Leap year")
