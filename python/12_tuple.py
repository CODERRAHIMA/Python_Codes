# tuple -> A built-in data type that lets us create immutable sequences of values.

tup = (1, 2, 3, 4)  # tup[0], tup[1]..
print(tup)
print(tup[0])
print(tup[1])


# tup[0] = "43" -> not allowed to assign new value on tuple like string in python

# single element tuple
tup2 = (1,)
print(tup2)

# empty tuple
tup3 = ()
print(tup3)

# tuple slicing is just like string and list slicing
tup4 = (1, 2, 3, 4)
print(tup4[1:3])
print(tup4[:2])
print(tup4[1:])
print(tup4[-3:-1])  #negative slicing