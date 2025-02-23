# Chapter 4 page - 50
# magicians = ['alice', 'david', 'carolina'] 
# for magician in magicians:     #like for i in `cat file.txt` The : is for start of loop
#     #print(magician)
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")
# #once for loop is done, it will print below message - Identaion is important
# print("Thank you, everyone. That was a great magic show!")
# print(f"I can't wait to see your next trick, {magician.title()}.\n")  #last value of magician is carolina

#TIY page 56
#4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
# pizzas = ['margherita', 'pepperoni', 'veggie']
# for pizza in pizzas:
#     print(pizza)
#     print(f"I like {pizza.title()} pizza.")
# print("\nI really love pizza!")

# Animals = ['dog','cat','rabbit']
# for animal in Animals:
#     print(animal)
#     print(f"A {animal} would make a great pet.")
# print("\nAny of these animals would make a great pet!")

# Making numerical list
#for value in range(1,5): #because of off_by_one behavioour prints from 1 to 4
    #print(value)
#for number in range(6):  #range(6) means 0 to 5
    #print(number)
#numbers = list(range(1,5))   #start from 1 till 4 (off_by_one)
#print(numbers)
#even_numbers = list(range(2,11,2))  #prints with addition of two - even numbers
#print(even_numbers)
# squares = []
# for value in range(1,11):
#     #square = value ** 2   #python takes ** as power of (like 2^2)
#     #squares.append(square)
#     squares.append(value**2)   #gives same answer in one line of code  
# print(squares)           
# print(min(squares))     #play with list of numbers mathematically
# print(max(squares))
# print(sum(squares))
#Using List comprehensions
#squares = [value**2 for value in range(1,11)]  #Here : is not req at end of for statement
#print(squares)

#TIY page - 60
#for i in range(1,):
#    print(i)
# million = []
# for value in range(1,1000001):
#     million.append(value)
# print(million[-1])
# print(max(million))
# print(min(million))
# print(sum(million))
# multiple_of_three = []
# for number in range(1,31):
#     multiple_of_three.append(number*3)
# print(multiple_of_three)
#cube = []
# for number in range(1,11):
#     # value = number**3
#     # print(f"Cube of {number} is {value}")
#     # cube.append(value)
#print(cube)
# cube = [value**3 for value in range(1,11)]    # Using Comprehension
# print(cube)

#working with part of list
#Players = ['charles','martina','michael','florence','eli']
# # print(Players[0:]) #prints from 0 till last
# # print(Players[1:3]) #prints from 1 till 2
# # print(Players[:4])  #prints from 0 till 3
# # print(Players[-3:]) #prints from -3 till last
# print("Here are the first three players on my team:")
# for player in Players[0:3]:
#     print(f"\t{player.title()}")

#Copying a list
#my_foods = ['pizza','falafel','carrot cake']
#friends_foods = my_foods[:] #[:] is used to copy the list
# print("My favourite foods are:")
# print(my_foods)
# print("\nMy friend's favourite foods are:")
# print(friends_foods)
#my_foods.append('cannoli')
#friends_foods.append('ice cream')
# print(f"\nMy favourite foods are: {my_foods}")
# print(f"\nMy fried's favourite foods are: {friends_foods}")
#If we don't use [:] then both lists will be same  > friends_foods = my_foods

## TIY page - 66
# print(f"The first three players in the list are: {Players[0:3]}")
# print(f"Three foods from middle of the list are: {my_foods[1:]}")
# print(f"The last three players in the list are: : {Players[-3:]}")
# Players.append('shahid')
# my_foods.append('biryani')
# print(f"The favourite food of {Players[-1]} is {my_foods[-1]}")
# # for player in Players[0:3]:
# #     for food in my_foods[0:3]:
# #         print(f"\n{player.title()} likes {food.title()}")
# for i in range(0,3):   #Good Thing to remember
#     print(f"{Players[i].title()} like {my_foods[i].title()}")

#Tuples - Immutable List > use () instead of []
# dimensions = (200,50)
# print(dimensions[0])
# dimensions[0]=(300) #This will give error because tuple is immutable
# You can play with tuple as is like list just you cant change the values

#TIY page - 68
# buffet = ('biryani','pizza','burger','past','kabab')
# # for food in buffet:
# #     print(food)
# #buffet[2] = 'sandwich' #This will give error because tuple is immutable
# buffet_new =('biryani','pizza','burger','past','kabab','sandwich')
# for food in buffet_new:
#     print(food)
