#function definition
def add(a,b):
    return a + b

print(add(13,21))


def average(a,b,c):
    return (a+b+c)/3

print(average(10,20,30))


heros = ["spiderman", "batman", "ironman", "superman"]
def print_heroes(heroes):
    for hero in heros:
        print(hero,end=" ")
    
print_heroes(heros)
print()

def fectorial(n):
    fact=1
    for i in range(1,n+1):
        fact *= i
    return fact
    
print("Fectorial:",fectorial(5))
