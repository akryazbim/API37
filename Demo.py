



"""
123 is my notes for the class
456
876
"""

#He's "The King"

#"He's"
#'"The King"'


# path = r"C:\Users\Akryazz\OneDrive\Documents\My Files\Revit Api Training\Python Revit API Training"

# a1 = "He\'s \"The King\""


# x = "Hello\tHI"

# #contains condition
# text1 = "How are you"


#print("how" not in text1)








#Condition Statement

# a = 100
# b = 1000

#ctrl+/
# if a>b:
#     print("a is greater than b")  
#     print("A")
# elif a==b:
#     print("a is equal to b")
# elif b>a:
#     print("b is greater than a")
#     print("B")


# x = 85

# if x>50:
#     print("x is greater than 50")
# elif x>75:
#     print("x is greater than 75")
# elif x>100:
#     print("x is greater than 100")
#elif x == 50:
#     print("x is equal to 50") 
# else:
#     print("Less than 50")


# if x>50 and x>100 and x>150:
#     print("x is greater than 50 and 100 and 150")
# elif x>50 and x>100:
#     print("x is greater than 50 and 100")
# elif x>50:
#     print("x is greater than 50")








# score = 94


# if score >= 35:
#     print("You have passed the exam")
#     if score >= 90:
#         print("Grade 1")
#         if score >= 95:
#             print("Excellent")  
#     elif score >= 80:
#         print("Grade 2")
#     else:
#         print("Grade 3")
# else:
#     print("You have failed the exam")



# studentName = "Sujan"

# if studentName == "Mariram":
#     print("You're awesome!")
# else:
#     print("You're also awesome!")



# academy = "EngineeringEra"

# if "BIM" in academy:
#     print("This is a BIM academy")
# else:
#     print("This is not a BIM academy")



#You get duct, width, if, action


#print("End of the program")




#List

# myList = [ 10, 20, 30, 31.56, 50.23, "Hello", True, 20-45, 10>5 and 5>10]




# #             0         1           2         3          4          5        6
# students = ["Atish", "Tanveer", "Ratnesh", "Santanu", "Panchal", "Devai", "Shazeb"]

# # students.append(105)
# #students.append("Naresh")

# #students.insert(-1, 50>25)

# #students.remove("Devai")
# #students.pop(2)

# #del students[3]

# print(students[0:3]+students[4:7]) 






# score = 94

# if score >= 35:
#     print("You have passed the exam")
#     if score >= 90:
#         print("Grade 1")
#         if score >= 95:
#             print("Excellent")
#     elif score >= 80:
#         print("Grade 2")
#     elif score >= 70:
#         print("Grade 3")
#     else:
#         print("Grade 4")
# else:
#     print("You have failed the exam")

# print("End of the program")


# students = ["Atish", "Tanveer", "Ratnesh", "Santanu", "Panchal", "Devai", "Shazeb"]

# #students.append("Imran")
# students.insert(3, "Imran")

# print(students)





#[1..5]

#print(list(range(1,6)))

#10 == 5
# 10 = 5

# i = 1

# while i <= 5:
#     print(i)
#     print("Hi")
#     a = 10
#     print(a*i)
#     i = i+1



# i = 6

# while i >= 10:
#     print("Pass")
#     i += 1



# i = 10

# while i >= 1:
#     print(i)
#     i = i-1 
#     #i -= 1

# i = "a"

# while i != "aaa":
#     print(i)
#     i = i + "a"


# print("End of loop")


#null or None


# num = int(input("Enter a positive number:"))

# while num <= 0:
#     print("Enter a valid number!")
#     num = int(input("Enter a positive number:"))

# print(num)


# x = 53

# if x%2 != 0:
#     print("Odd")
# else:
#     print("Even")









# i = 1
# while i <= 10:
#     if i%2 == 0:
#         print(i)
#     i += 1




# i = 1
# total = 0
# while i <= 5:
#     total = i + total
#     i = i + 1

# print(total)
# #1+2+3+4+5

#print(sum(range(1,6)))



# students = ["Atish", "Tanveer", "Ratnesh", "Santanu", "Panchal", "Devai", "Shazeb"]

# # abc = 0
# # while abc < len(students):
# #     print(students[abc])
# #     abc += 1

# for xyz in students: 
#     if xyz == "Tanveer" or xyz == "Santanu":
#         print("Hello " + xyz)

#ctrl + /


#print the sum of all even numbers between 1 to 500 using while loop and for loop



# i = 2

# total = 0

# evenNumbers = []

# count = 0

# while i <= 500:
#     evenNumbers.append(i)
#     count += 1
#     total += i
#     i = i+2

# print("Sum of all even numbers: ", total)
# print(len(evenNumbers))
# print("Count: ", count)


# students = ["Atish", "Tanveer", "Ratnesh", "Santanu", "Panchal", "Devai", "Shazeb"]
# students.append("NEw value")

#[2,4,6,8,10,12,14,16,18,20.........]
#[1,3,5,7]
# total = 0

# for i in range(1, 501, 2):
#     total = total + i

# for i in range(1, 501):
#     if i%2 != 0:
#         total = total + i

# print("Sum of all odd numbers: ", total)



# students = ["Atish", "Tanveer", "Ratnesh", "Santanu", "Panchal", "Santanu", "Devai", "Shazeb" ]


# # for i in students:
# #     if i == "Santanu":
# #         print("I found Santanu")
    
# for i in students:
#     if i != "Santanu":
#         continue
#     print(i)





# print("START")


# def greet():
#     print("Hi all")
#     print("How are you?")
#     print("What's the last movie you watched")

# print("END")

# x = 10
# y = 20

# print(x+y)

# greet()



# movies = ["gajini", "jailer", "F&F", "golmal", "coolie"]

# print(len(movies))


# movies.append("Titanic")

# print(len(movies))



# movies = ["gajini", "jailer", "F&F", "golmal", "coolie"]


# for movie in movies:
#     if movie == "gajini":
#         continue
#     print(movie)







# print("START")


# def greet():
#     print("Hi all")
#     print("How are you?")
#     print("What's the last movie you watched")

# greet()

# print("END")





# def add():
#     a = 25
#     b = 50
#     print(a+b)

# a = 100

# add()

# print(a)
# print(b)



# def sub(a=5, b=0):
#     print(a-b)

# result = sub(50,40)

# print(result+15)


# def divide(a,b):
#     return a/b


# result = divide(10,2)

# print(result+50)





#10+15+15+620+90



# def add(*nums):
#     total = 0
#     for n in nums:
#         total += n

#     return total


# print(add(10,20,40,50,60,70,90,100))

#void 
#return type


#def DoClashDetection():
#..............
#.............
#.............


#def DoAndReturnClashes:
#......
#.....
#....
#return result






#Class -> Properties, methods(fuctions)

#Object

#Namespaces


#OOPs


class Person:
    Name = "Santanu"
    Age = 25

    def Study(self):
        print("Santanu is studying")


p1 = Person()

p1.Study()