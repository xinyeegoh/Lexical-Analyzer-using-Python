
# NUMBERS, IDENTIFIERS, STRINGS

# detect different types of numbers
x = 7.6E+90 
b = 60 
c = 90.567
d = 90E+23

#detect different types of identifiers and strings 
abcd = "hello" # strings no space
m = "bye bye bye " #strings with space
abcd_989ki = "^jdjdd *) //} ^78 " #strings with mixed symbols/operators
id_dhdh = 'sjsj ]]] [[[' #strings with '...'

#ERROR handling invalid identifier
78sgsg 

#detect identifiers separated by comma
abcd, m, id_dhdh, abcd_989ki

# detect lines with perfect spacing
a = 1
b = 5
c = 6

#detect lines with mixed spacing
d = (b**2) - (4 *a* c)

#detect lines with no spacing
sol1=(-b-cmath(d))/(2*a)

#detect strings from lines no spacing
print('The solution are {0} and {1}'+sol1)

#detect strings for both "..." and '...' with different spacing
print("this is a string")
print('this is a string')

print("string number 1" + 'string number 2')
print   (    "string number 1"+ 'string number 2')
print( "string number 1 "  +'string number 2' )
print("\n")
#detect strings from lines with enclosed "print"
print("print('jjdjdj')")