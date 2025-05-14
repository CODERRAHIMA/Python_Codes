# when function calls itself repeatedly
def show(n):
    if n == 0:
        return
    print(n, end=" ")
    show(n - 1)

show(5)
print()


# return n!
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

print(fact(5))



def print_list(list, i=0):
    if i == len(list):
        return
    print(list[i], end=" ")
    print_list(list, i + 1)


fruits = ["apple", "banana", "cherry"]
print_list(fruits)
