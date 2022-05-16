
#RESERVED WORDS
#EXAMPLES ONLY, NOT EXACTLY RUNNABLE

from smth import smth

class Example123():
    def divide(x, y):
        try:
            print(f'{x}/{y} is {x / y}')
        except ZeroDivisionError as e:
            print(e)
        else:
            print("divide() function worked fine.")
        finally:
            print("close all the resources here ")
            return x


def example234():
    for i in j:
        i+=1
        global z
        z=   j%i
        if    z<  12:
            continue
        if z>12 :
            break

if i==0 or i >= 9 :
    i += 1
elif i <= 7 and not i == 9:
    i -=1
else :
    i = 0

with open('output.txt') as file: 
    print('FILE OPENED !')

v = lambda w: w*2
for v in range(1,6):
    print((v))

#will not detect "whilecheck_value" having reserved word "while"
whilecheck_value(pay)==True 

while i== None :
    print("Hello")

x = [1,2,3]
y = [1,2,3]
assert x == 0
print(x is y)
del x


    