
#SYMBOLS, OPERATORS 

#ERROR handling invalid symbol/operators
$ @ 


a=1
b = 2
c= 3
d =4

#detect [] list bracket operator 
list = [1,2,2]
list_1 =[ 2, 6 , 7]

#detect symbols / operators with different spacing
a = (b+c) %d - 89+44
a = b / c*d- 9 + 6
{[(0)]} !

~a

#detecting & && | || operators and other operators
# note: && and || aren't valid operators for python, so these are pseudo
if a!=1&b==5:
    c = 7
    print("awesome")
if a >= 1 && b > 5:
    c=7
if a <=1 | b<5:
    c =7
if a==1 ||b == 5 :
    c= 7




