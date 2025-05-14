# for loops
# nums = [1, 2, 3, 4, 5]
# for i in nums:
#     print(i)

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
x = 49
i = 0
for val in tup:
    if val == x:
        print("Found at index", i)
    i += 1
