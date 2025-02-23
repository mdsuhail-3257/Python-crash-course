# my_list = [1, "hello", 3.14, True]
# print(my_list)  #givese the complete list
# print(my_list[0])  #gives the first element of list
# print(my_list[-1])  #gives the last element of list
# print(my_list[1:])  #gives the list from 1st element to last element
# print(my_list[1:3])  #gives the list from 1st element to 3rd element
# my_list[0] = 2  #change the 1st element of list

# bicyles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicyles[-1].title())  #gives the last element of list
# print(bicyles[-2].lower())  #gives the 2nd last element of list and so on
# print(bicyles[3].upper())
# # last values are often used if you don't know the length of list
# ## Following is to use Individual values from list
# message = f"My first bicycle was a {bicyles[0].title()}"
# print(message)

# #exercise page-36
# names = ["Mohammad", "Suhail", "Shaikh"]
# print("My first name is",names[0])
# print("My last name is",names[-1].upper())
# fav_cars = ["Audi", "BMW", "Mercedes", "Jaguar"]
# print("My favourite cars are",fav_cars[1],"and",fav_cars[-1])
# fav_cars[0] = "Audi Q7"  #change the 1st element of list
# print(fav_cars)

#append() method is used to add the element at the end of list
# fav_cars.append("Audi A8")  #append the element at the end of list
# print(fav_cars)
#insert() method is used to insert the element at the specified index
# fav_cars.insert(1, "Audi A6")  #insert the element at 1st index
# print(fav_cars)
# del fav_cars[1]  #delete the element at 1st index
# print(fav_cars)
# motorcycles = []   #create an empty list and append the elements dynamically
# motorcycles.append("honda")
# motorcycles.append("yamaha")
# motorcycles.append("suzuki")
#print(motorcycles)
#del() method is used to remove the element from the list
#del motorcycles[0], motorcycles[1]  #delete the elements at 0th and 1st index
#print(motorcycles) #once elemets deleted it cannot be retrieved
#pop() method is used to remove the last element of the list and lets you work with it like popping up on removed element
#popped_motorcycle = motorcycles.pop()
#print(motorcycles) #gives the list after removing the last element
#print(popped_motorcycle)  #gives the removed element
#pop() method can also be used to remove the element at specified index
#last_owned = motorcycles.pop()
#print(f"The last motorcycle I owned was a {last_owned.title()}.")
#print(f"My first owned morotcycle was a {popped_motorcycle.title()}.")
#print(motorcycles)
#remove() method is used to remove the element by value   #page - 42
# motorcycles.append("ducati")
# print(motorcycles)
# too_expensive = "ducati"
# motorcycles.remove(too_expensive)  #use when you don't know the index of element
# print(f"\nA {too_expensive.title()} is too expensive for me.")
# print(motorcycles)

#Exercise page-42
# invited_people = ["Robert", "John", "Sara", "Mike", "Juneyed","zeyneb"]
# print(f"I would like to invite {invited_people[0]} to dinner")
# print(f"I would like to invite {invited_people[1]} to dinner")
# print(f"I would like to invite {invited_people[2]} to dinner")
# print(f"I would like to invite {invited_people[3]} to dinner")
# print(f"I would ike to invite {invited_people[4]} and {invited_people[5].title()} for dinner")
# cant_come = "Sara"
# invited_people.remove(cant_come)
# print(f"\nI think {cant_come} can't come for dinner")
# invited_people.insert(2, "Ali")
# print(f"\n I would like to invite {invited_people[0]} to dinner")
# print(f"I would like to invite {invited_people[1]} to dinner")  
# print(f"I would like to invite {invited_people[2]} to dinner")
# print(f"I would like to invite {invited_people[3]} to dinner")
# print(f"I would like to invite {invited_people[4]} and {invited_people[5].title()} for dinner")
# print("\nI found a bigger table so I am inviting more people")
# invited_people.insert(0, "Shahid")
# invited_people.insert(3, "Suhail")
# invited_people.append("Zain")
# print(invited_people)
# print(f"\nI would like to invite {invited_people[0]} to dinner")
# print(f"I would like to invite {invited_people[1]} to dinner")
# print(f"I would like to invite {invited_people[2]} to dinner")
# print(f"I would like to invite {invited_people[3]} to dinner")
# print(f"I would like to invite {invited_people[4]} to dinner")
# print(f"I would like to invite {invited_people[5]} to dinner")
# print(f"I would like to invite {invited_people[6]} and {invited_people[7]} to dinner")
# print(f"I would like to invite {invited_people[8]} to dinner")

# print("\nI can only invite two people for dinner")
# uninvited_people = invited_people.pop()
# print(f"Sorry {uninvited_people} I can't invite you for dinner")
# uninvited_people = invited_people.pop(0)
# print(f"Sorry {uninvited_people} I can't invite you for dinner")
# uninvited_people = invited_people.pop(1)
# print(f"Sorry {uninvited_people} I can't invite you for dinner")
# uninvited_people = invited_people.pop(2)
# print(f"Sorry {uninvited_people} I can't invite you for dinner")
# print(invited_people)
# uninvited_people = invited_people.pop(0)
# print(f"Sorry {uninvited_people} I can't invite you for dinner")
# print(invited_people)
# uninvited_people = invited_people.pop(0)
# print(f"Sorry {uninvited_people} I can't invite you for dinner")
# print(invited_people)
# del invited_people[0]
# print(invited_people)
# print(f"I would like to invite {invited_people[0]} and {invited_people[1]} to dinner")

#sort() method is used to sort the list in alphabetical order
# cars = ["bmw", "audi", "toyota", "subaru"]
# cars.sort()
# print(cars)
# cars.sort(reverse=True)  #sort the list in reverse order
# print(cars)
# #sorted() method is used to sort the list temporarily
# cars = ["Bmw", "Audi", "Toyota", "Subaru"]
# print("Here is the original list:")
# print(cars)
# print("\nHere is the sorted list:")
# print(sorted(cars))
# print("\nHere is the original list again:")
# print(cars)
# #reverse() method is used to reverse the list
# cars.reverse()
# print(cars)
# #len() method is used to find the length of list
# print(len(cars))

#Exercise page-46
# places = ["Paris", "London", "New York", "Dubai", "Istanbul"]
# print(f"This is original list {places}")
# print(f"This is sorted list {sorted(places)}")
# print(f"This is original list {places} again")
# print(f"This is sorted list in reverse order {sorted(places, reverse=True)}")
# print(f"This is original list {places} again")
# places.sort()
# print(f"This is sorted list {places}")
# print(places)
# print(f"This is sorted list in reverse order {sorted(places,reverse = True)}")
# places.reverse()
# print(len(places))




