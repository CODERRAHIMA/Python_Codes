# similar to string slicing

# list_name[starting_idx:ending_idx]  -> ending idx is not included
# list_name[ i : j ]   will be print  from i to (j-1)

marks = [94.5, 87.5, 95.5, 66.5, 45.5]
print(marks[1:4])  # will show index [1][2][3]
print(marks[:4])  # by default starting index is 0
print(marks[1:])  # by default ending index is last

# negative indexing same as string
print(marks[-3:-1])  # will show index[-3][-2]
