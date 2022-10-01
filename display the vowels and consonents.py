def Check_Vow(string, vowels):
        final = [each for each in string if each in vowels]
        print(len(final))
        print(final)
string =input("Enter the words: ")
vowels = "AaEeIiOoUu"
def Check_Con(string, consonants):
        final2 = [each for each in string if each in consonants]
        print(len(final2))
        print(final2)
consonants = ("bcdfghjklmnpqrstvwxyz")
Check_Vow(string, vowels);
Check_Con(string, consonants);
