#1 string and numeric values can operate together with *
a, b = 2, 3   # a=2, b=3
txt = "@$"
print (a*txt*b)  # print txt string a*b times or 6 times


#2 string and string can operate with +
c, d = "2", 3
txt = "r$"
print ((c+txt)*d)  # add two string = concatenation


#3 numeric values can operate with all arithmetic operators
a, b = 2, 3
c = 4
print (a+b*c)


#4 arithmetic expression with int and float will result in float
a, b = 2, 3.0
c = 4
print (a+b*c)


#5 result of division operator with two int will be float
a, b = 1, 2
c = a/b
print (c) 


#6 integer division of float & int will give int but displayed as float
a, b = 1.5, 3
c = a//b
print (c)  # floor value of 1.5/3


#7 floor gives closest integer which is lesser than or equal to the float value
a, b = 12, 5
c = a//b
print (c)

a, b = -12, 5
c = a//b
print (c)

a, b = 12, -5
c = a//b
print (c)


#8 remainder is negative when denominator is negative
# modulo  n%d  ->   n = numerator, d = denominator
# when  n+,d- = -ve    n+,d+ = +ve  n-,d- = +ve  n-,d+ = +ve
a, b = -5, 2
c = a%b
print (c)

a, b = 5, 2
c = a%b
print (c)

a, b = 5, -2
c = a%b
print (c)