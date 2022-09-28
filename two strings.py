s1=str(input("enter the string"))
s2=str(input("enter the string"))
def shared(s1, s2):
  find = 0
  for letter in s1:
      if letter in s2:
          find += 1
  return find
print(shared(s1, s2))
