collection = {1, 2, 3, 4, "hello", "world", "world", 4, 4}

print(collection)  # set ignores duplicate values
print(len(collection))

# empty set
empty_set = set()
print(empty_set)


# set Methods
new_set = {1, 2, 3, 4, 3, 5}

new_set.add(6)  # adds an element
new_set.add(7)
print(new_set)

new_set.remove(3)  # removes the element
print(new_set)

print("poped value:", new_set.pop())  # removes a random value
print("poped value:", new_set.pop())


new_set.clear()  # empties the set
print(new_set)
print(len(new_set))


# set union and intersection method
set1 = {1, 2, 3}
set2 = {2, 3, 4}

union_set = set1.union(set2)  #combines both set values & returns new
print(union_set)

intersection_set=set1.intersection(set2)   #combines common values & returns new
print(intersection_set)