# data = f.read( ) -> reads entire file
# data = f.readline( ) -> reads one line at a time
# f.write( “this is a new line") -> writes a new line


# (question_1)Create a new file “practice.txt” using python. Add the following data in it:
# Hi everyone
# we are learning File I/O
# using Java
# i like programming in Java
# solution_1:
# with open("practice.txt", "w") as f:
#     f.write("Hi everyone\nwe are learning File I/O\nusing Java\ni like programming in Java\n")


# (question_2)WAF that replace all occurrences of “java” with “python” in above file.
# solution_2:
# with open("practice.txt", "r") as f:
#     data = f.read()
# new_data = data.replace("Java", "Python")
# print(new_data)

# with open("practice.txt", "w") as f:
#     f.write(new_data)

# (question_3)Search if the word “learning” exists in the file or not.
# solution_3:
# word = "learning"
# with open("practice.txt", "r") as f:
#     data = f.read()
# if(word in data):
#     print("found")
# else:
#     print("not found")


# (question_4)WAF to find in which line of the file does the word “learning”occur first.Print -1 if word not found.
# solution_4:
# word = "learning"
# data = True
# line_no = 1
# with open("practice.txt", "r") as f:
#     while data:
#         data = f.readline()
#         if word in data:
#             print(line_no)
#             break
#         line_no += 1
#     else:
#         print(-1)

# (question_5)From a file containing numbers separated by comma, print the numbers.
# solution_5
# with open("numbers.txt","r") as f:
#     data=f.read()
#     print(data)

#     num=""
#     for i in range(len(data)):
#         if(data[i]==","):
#             print(num)
#             num=""
#         else:
#             num+=data[i]


# (question _6)From a file containing numbers separated by comma, print the count of even numbers.
# solution_6
# with open("numbers.txt", "r") as f:
#     data = f.read()
#     print(data)

#     num = ""
#     for i in range(len(data)):
#         if data[i] == ",":
#             num = int(num)
#             if num % 2 == 0:
#                 print(num)
#             num = ""
#         else:
#             num += data[i]
