# slicing = accessing parts of a string
# str[ staring_idx : ending_idx ]   - ending idx is not included
# str[ i : j ]   will be print  from i to (j-1)

name = "Rahima"
slice1 = name[0 : 3]  # first 3 idx = [0] [1] [2] = Rah
print (slice1)
slice2 = name[2 : 5]  # idx 2 3 4 = him
print (slice2)

print (name[3 : len(name)])  # idx[3] to last
print (name[ :4])   # [0 : 4]
print (name[3: ])   # [3 : len(name)] = [3 : last]


# Negative index in slicing
# name = rahima -  a=-1 m=-2 i=-3 h=-4 a=-5 R=-6 
# str[-j : -i]  will be print  from -j to (-i-1)
name3 = "rahima"
print (name3[-4 : -1])
