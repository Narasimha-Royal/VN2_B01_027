'''
    String :
A String is sequence of alphabets, characters, numbers, words.
A String can be created using single quotes or bouble quotes or even triple quotes.'''


print("---------String Functions---------")

a = 'naRaSimha roYal'
b = 'sImhA'

print("Given String is :", a)

print("------1) Using Capitalize Function------")#Converts the first character to upper case in Given String
print("After applying Capitalize Function for given string :--", a.capitalize())

print("------2) Using Center Function-------")        #Returns a centered string for given string
print("After applying Center Function for given string :--", a.center(30,'@'))

print("-----3) Using Count Function-------")     #Returns the number of times a specified value occurs in a given string
print("Number of a's present in the string :--", a.count('a'))
print("Number of r's present in the string :--", a.count('r'))
print("Number of R's present in the string :--", a.count('R'))

print("------4) Using Encode Function--------")                 #Returns an encoded version of the string
print("After applying Encode Function for given string:--", a.encode())

print("------5) Using Casefold Function------")   #Converts string into lower case
print("After applying Casefold Function for given string:--", a.casefold())

print("------6) Using Endswith Function------")      #Returns true if the string ends with the specified value
print("After applying Endswith Function with 'l' letter:--", a.endswith('l'))
print("After applying Endswith Function with 'a' letter:--", a.endswith('a'))

d = "This\tis\tpython\tprogram"
print("-------7) Using Expandtabs Function---------")     #Sets the tab size of the string
print("After applying Expandtabs Function for given string:--", d.expandtabs(7))

print("-------8) Using Find Function--------")     #Searches the string for a specified value and returns the position of where it was found
print("Index of 'Simha' present in given string :--", a.find('Simha'))
print("Index of 'roYal' present in given string :--", a.find('roYal'))
print("Index of 'Royal' present in given string :--", a.find('Royal'))

print("-------9) Using Isalnum Function--------")       #Returns True if all characters in the string are alphanumeric
print("'naRaSimha roYal' string is only alphanumeric string :--", a.isalnum())

print("-------10) Using Isalpha Function-------")    #Returns True if all characters in the string are in the alphabet
print("'naRaSimha roYal' string is only alphabets string :-- ", a.isalpha())

print("-------11) Using Isdecimal Function-------")   #Returns True if all characters in the string are decimals
print("'naRaSimha roYal' string is only decimals string :--", a.isdecimal())

print("------12) Using Isdigit Function--------")    #Returns True if all characters in the string are digits
print("'naRaSimha roYal' string in only digits string :--", a.isdigit())

print("--------13) Using Isidentifier Function------")   #Returns True if the string is an identifier
print("Given string is only identifier string :--",a.isidentifier())

print("------14) Using Islower Function-------")     #Returns True if all characters in the string are lower case
print("Given String contain only lower case letters :--", a.islower())

print("------15) Using Isnumeric Function-----")       # Returns True if all characters in the string are numeric
print("Given string contain only numbers :--", a.isnumeric())

print("------16) Using Isspace Function--------")      #Returns True if all characters in the string are whitespaces
print("Given string contain only space :--", a.isspace())

print("------17) Using Isupper Function--------")     #Returns True if all characters in the string are upper case
print("Given string contain only upper case letters :--", a.isupper())

print("------18) Using Join Function--------")    #Joins the elements of an iterable to the end of the string
print("Join given Two strings :--", a.join(b))

print("------19) Using Lower Function-------")     #Converts a string into lower case
print("After conversion of given string into lowercase letters :--",a.lower())

print("-----20) Using Lstrip Function-------")     #Returns a left trim version of the string
c = '^^^^^Royal^^^^^'
print("Lstrip for given string :--", c.lstrip('^'))

print("------21) Using Rstrip Function------")     #Returns a right trim version of the string
print("Rstrip for given string :--", c.rstrip('^'))

print("------22) Using Replace Function------")    #Returns a string where a specified value is replaced with a specified value
print("Replace 'a' with '@' in given string :--", a.replace('a', '@', 2))
print("Replace 'a' with '@' in given string :--", a.replace('a', '@'))
print("Replace 'a' with '@' and 'o' with '&' in given string :--", a.replace('a', '@').replace('o', '&'))

print("-----23) Using Split Function--------")      #Splits the string at the specified separator, and returns a list
print("String after split :--", a.split())

print("----24) Using Strip Function--------")      #Returns a trimmed version of the string
print("Given String after Strip :--", c.strip('^'))

print("-----25) Using SwapCase Function-----")   #Swaps cases, lower case becomes upper case and vice versa
print("Given string after 'Swapcase'   :--", a.swapcase())

print("-----26) Using Title Function-------")   #Converts the first character of each word to upper case
print("Given string after applying 'Title' function :--", a.title())

print("-----27) Using Upper Function------")   #Converts a string into upper case
print("Given string after applying 'Upper' function :--", a.upper())

m = "This {} Vn2Solutions"
print("-----28) Using Format Function------")  #Formats specified values in a string
print("After applying Format Function given string is :--", m.format('is'))

print("-----29) Using Index Function-------")   #Searches the string for a specified value and returns the position of where it was found
print("Index of 'Y' in given string :--", a.index('Y'))

print("----30) Using Isprintable Function------")   #Returns True if all characters in the string are printable
print("Checking given string is printable or not :--", a.isprintable())

print("-----31) Using Istitle Function--------")   #Returns True if the string follows the rules of a title
print("Checking given string is Title or not :--", a.istitle())

print("-----32) Using Ljust Function-----")     #Returns a left justified version of the string
print(a.ljust(40), "After applying LJust Function")

print("-----33) Using Partition Function----")   #Returns a tuple where the string is parted into three parts
print("After partition at 'Simha' and given string is :--", a.partition('Simha'))

print("-----34) Using Maketrans Function----")  #Returns a translation table to be used in translations
s = a.maketrans("r", "R")
print(a.translate(s))

print("-----35) Using Rfind Function------")  #Searches the string for a specified value and returns the last position of where it was found
print("Index of 'a' at last occurrence :--", a.rfind('a'))

print("-----36) Using Rindex Function------")  #Searches the string for a specified value and returns the last position of where it was found
print("Index of 'Y' :--", a.rindex('Y'))

print("-----37) Using Rjust Function------")   #Returns a right justified version of the string
print(a.rjust(30))

print("-----38) Using Rpartition Function------")  #Returns a tuple where the string is parted into three parts
print(a.rpartition('Ya'))

print("-----39) Using Rsplit Function-----")   #Splits the string at the specified separator, and returns a list
print(a.rsplit('Y'))

print("-----40) Using Startswith Function")  #Returns true if the string starts with the specified value
print(a.startswith('na'))
