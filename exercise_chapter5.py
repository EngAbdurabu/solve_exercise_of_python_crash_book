# 5.1
car = 'Subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print(car != 'subaru')
print(car != 'bmw')
print(car == 'bmw')
print('-' * 100)

# 5.2
print('sre' == 'Sre')
print('sea' != 'Sea')
print(car.lower() == 'subaru')
print(4 == 4 and car == 'subaru')
print(4 == 4 or car == 'subaru')
name = ['Ahmed', 'Ali', 'Hussain', 'Saleh']
print('Ahmed' in name)
print('Ali' not in name)
print('-' * 100)

# 5.3
alien_color = 'green'
if alien_color == 'green':
	print("You are earned 5 Points")
print('-' * 100)

# easy 4-6

# 5.7
favorite_fruits = ['Apple', 'orange', 'strawberry']
if 'Apple' in favorite_fruits:
	print("You really like apple")

if 'orange' in favorite_fruits:
	print("You really like orange")

if 'banana' in favorite_fruits:
	print("You really like bananas")

if 'watermelon' in favorite_fruits:
	print("You really like watermelons")

if 'strawberry' in favorite_fruits:
	print("You really like strawberries")

print('-' * 100)

# 5.8 Hello Admin
usernames = ['Ahmed', 'Ali', 'Admin', 'Mohammed', 'Saleh']
for username in usernames:
	if username == 'Admin':
		print(f"************************************\nHello {username.upper()},"
		      f" would you like to see a status "
		      f"report?\n******************************************")
	else:
		print(f"Hello : {username} Welcome to our website")

print('-' * 100)
# 5.9 No users
users = []
if users:
	print(f"Welcome {users} to our website")
else:
	print("We need to find soe users!")

print('-' * 100)
# 5.10 checking usernames
current_users = ['Ahmed', 'Mohammed', 'Ali', 'Saleh', 'Majid']
new_users = ['Ahmed', 'Salem', 'Saleh', 'Majid', 'Hussain']
for new_user in new_users:
	if new_user in current_users:
		print("the person will need to enter a new username")
	else:
		print("the username is available ")

print('-' * 100)

# 5.11 ordinal Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in reversed(numbers):
	if number == 9:
		print('1st \n2nd \n3rd \n4th \n5th \n6th \n7th \n8th \n9th\n')
	elif number == 8:
		print('\n1st \n2nd \n3rd \n4th \n5th \n6th \n7th \n8th\n')
	elif number == 7:
		print('\n1st \n2nd \n3rd \n4th \n5th \n6th \n7th\n')
	elif number == 6:
		print('\n1st \n2nd \n3rd \n4th \n5th \n6th\n')
	elif number == 5:
		print('\n1st \n2nd \n3rd \n4th \n5th\n')
	elif number == 4:
		print('\n1st \n2nd \n3rd \n4th\n')
	elif number == 3:
		print('\n1st \n2nd \n3rd\n')
	elif number == 2:
		print('\n1st \n2nd\n')
	else:
		print('\n1st \n')

print('-' * 100)
# 5.12 My idea ( small project )
user_courses = []
if user_courses:
	print("no one want course")
else:
	user_courses.append(input("Enter the course you want : ").lower())
My_course = ['python', 'html ', 'css', 'icdl', 'completed communication ']
if user_courses == 'python' or user_courses == 'html' or user_courses == 'css':
	print(f"Welcome to  course of {user_courses}, enjoy  ")
else:
	print(f"sorry this course of {user_courses} is not find now ")
