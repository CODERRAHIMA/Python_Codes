# string = data types that stores sequence of characters
# concatenation  "Rahima" + "Akter" = "RahimaAkter"
# length of a string->  len(str)

name1 = "Rahima"
name2 = "Akter"
add = name1+name2
print (add)
length = len(name1)
print (length)      # 4 length
add2 = name1 + " " + name2
print (add2)
print(len(add2)) 


# indexing
# indexing = strigns characters position sequentially
# str = "rahima" -> indexing  str[0]=r  str[1]=a  str[2]=h  str[3]=i
# indexing always starts at [0]

name = "Rahima"
name[0]
name[1]
print (name[1])

# name[2] = "d"  not allowed to assign new value on string in python


#Slicing
#slicing = accessing parts of a string
# str[ staring_idx : ending_idx ]   -> ending idx is not included
# str[ i : j ]   will be print  from i to (j-1)

name="Rahima"
print(name[1:4]) #will show index[1][2][3]
print(name[2:])  #by default ending index is last
print(name[:4])  #by default starting index is 0

#negative slicing
str="Rahima"
print(str[-3:-1])
