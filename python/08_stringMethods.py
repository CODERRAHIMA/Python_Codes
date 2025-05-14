
str = "raha is sooo Pretty!"

# return True if str ends with substring "er."
str.endswith("ty!")
print (str.endswith("ty!"))

# capitilize 1st character and small others
str.capitalize()
print (str.capitalize())
print (str)  # 2nd time doesn't work
str = str.capitalize() # for permanet change in str
print (str)

# Now str = "Raha is sooo pretty!"
str = "Raha is sooo pretty!"

# replaces all occurances of old char in new char
str.replace("o", "u")
print (str.replace("o", "u"))
print (str.replace("pretty", "cute"))

str = "Raha is sooo pretty & sooo cute!"
print(str)

# find the word : return first index of first occurence
str.find("s")
print (str.find("s"))    # print first s idx
print (str.find("sooo")) # find first sooo's first idx

# counts the occurence of substring in a string
# number of occurences = count
str.count("sooo")
print(str.count("sooo"))
print (str.count("o"))
