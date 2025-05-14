list = [2, 1, 3]
list.append(4)  # adds one elementat the end
print("List after append:", list)

list.sort()  # sorts in ascending order
print("List after sort in ascending order:", list)

list.sort(reverse=True)  # sorts in descending order
print("List after sort in descending order", list)

list.reverse()  # reverse the list
print("List after reverse:", list)

# insert element in index
# list.insert(index,element)
list.insert(1, 100)
print("List after inserting element:", list)

list2 = [2, 1, 3, 1]
list2.remove(1)  #removes first occurrence of element
print(list2)


#removes element at index
#list.pop(index)
list2.pop(1)  
print(list2)
