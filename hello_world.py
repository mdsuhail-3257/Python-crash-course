'''Fibonacci series
message = "fibonacci series upto n"
def fib(n):
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b= b, a+b
	print()
fib(1000)
'''

''' using Methods to play with variables > titile(),upper(),lower()
msg = "Ada Lovelace" 
print(msg.title())
print(msg.upper())
print(msg.lower())
'''

''' full_name.py Use of variables in string , using f string to compose message and print 
first_name = "Mohammad"
middle_name = "Suhail"
last_name = "Shaikh"
full_name = f"{first_name} {middle_name} {last_name}"
print(full_name)  #prints as is
print(f"Hello, {full_name.upper()} :)")   #compose complete message using f-string
variable = f"Hello, {full_name.lower()} :)"   #compose the message and assign it to another variable then print it
print(variable)
'''

''' whitespaces.py 
print("pyhton")                             #print with no whitespaces(space,tab,end-of-line symbols)
print("\tpyhton")                           #add tab then print 
print("Languages:\npython\njava\nC\nC++")   #print each in next line
# In python "message" and "message " are different unless you tell otherwise  => Stripping Whitespace
right_space = "pyhton "
left_space =" pyhton"
fav_lang = "  pyhthon is my favourite Language  "
print(right_space.rstrip())                 #checks if there is any whitespace RIGHT side of message and removes it while printing
print(left_space.lstrip())                  #checks if there is any whitespace LEFT side of message and removes it while printing
print(fav_lang.strip())                     #removes whitespaces from both the side of message
'''

''' apostrophy.py  know where to use "" and where to use ''
message = "One of Python's strength is its diverse community"
print(message)
message  = 'One of Python's strength is its diverse community' #gives Syntaxerror
'''

'''exercise page-25
#----- print with double-quotes
print("Albert Einstein once said,",'"A person who never made a mistake never tried anything new."')
famous_person = "Albert Einstein"
q1 = '  \n"A person who never made a mistake'
q2 = 'never tried anything new.\t"   '
print(famous_person,"once said,",'"A person who never made a mistake never tried anything new."')
print(famous_person,"once said,",q1.lstrip(),q2.rstrip())
print(famous_person,"once said,",q1.strip(),q2.strip())
'''

