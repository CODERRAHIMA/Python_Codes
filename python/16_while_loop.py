# while loop
i = 1
while i <= 5:
    print(i)
    i += 1

print("while loop ended")


# Print the elements of the following list using a loop:
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0
while idx < len(list):
    print(list[idx])
    idx += 1


# Search for a number x in this tuple using loop:
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
x = 49
idx = 0
while idx < len(tup):
    if tup[idx] == x:
        print("Found at index ", idx)
    else:
        print("Finding...")
    idx += 1
