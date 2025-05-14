# Dictionaries are used to store data values in {key:value} pairs
dict = {
    "name": "Rahima", # "key":value
    "cgpa": 9.8, 
    "marks": [98, 97, 95]
}
print(dict)

#unordered, mutable(changable) and dont allow duplicate keys

#accessing values
print(dict["name"])
print(dict["cgpa"])

#changing value
dict["name"]="Raha"  #overwrite
print(dict)

#assigning value
dict["surname"]="Akter"
print(dict["surname"])

print(dict)

#empty Dictionary
dic={}
print(dic)


#nested Dictionary
student = {
    "name":"Rahima",
    "subjects":{
        "phy":97,
        "chem":95,
        "math":98
    }
}

print(student)
print(student["subjects"])
print(student["subjects"]["math"])
