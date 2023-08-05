# 4.1
paizzas = ['pizza vegetables', 'pizza chicken ', 'only pizza']
for paizza in paizzas:
	print(f"I like {paizza.title()}")
	print('I really love pizza\n')
print('How much you like pizza?')
print('-'*100)

# 4.2
animals = ['cat', 'dog', 'hamster']
for animal in animals:
	print(f"{animal.title()} would make a great pet ")
print('Any of these animals would make a great pet?')
print('-'* 100)

# 4.3
for count in range(1,21):
	print(count)
print('-'* 100)
'''
# 4.4
for milion in range(1, 1000001):
	print(milion)
print('-'* 100)

# 4.5
million = range(1, 1000001)
print(min(million), 'the minimum value ')
print('-'* 100)
print(max(million), 'this is maximum value ')
print('-'* 100)
print(sum(million), 'this is sum of all value from one to million ')
print('-'* 100)
'''
# 4.6
odd_number = list(range(1, 21, 2))
for odd in odd_number:
	print(odd)
print(odd_number)
print('-' * 100)

# 4.7
threes = [num * 3 for num in range(3, 31)]
print(threes)
print('-' * 100)

# 4.8
cubes = list(range(1, 11))
for cube in cubes:
	c = cube ** 3
	print(f" {cube} ^ 3 = {c}")
print('-' * 100)

# 4.9
cubes = [cube ** 3 for cube in range(1, 11)]
print('the cubes of number from one to ten is :', cubes)
print('-' * 100)

# 4.10
names = ['ahmed', 'ali', 'khalal', 'hussin', 'majid', 'mohammed', 'saleh']
print('Welcome my bast friend : ')
print(names[:3])
print('you are my favorite friend :')
print(names[3:6])
print('you are from my friend :')
print(names[-3:])
print('-' * 100)

# 4.11
paizzas = ['pizza vegetables', 'pizza chicken ', 'only pizza']
friend_paizzas = paizzas[:]
paizzas.append('fish pizza')
friend_paizzas.append('fresh pizza')

print('these are my favorite pizza : ')
for my_pizza in paizzas:
	print(my_pizza)

print("\nthese favorite pizza of my friend :")
for friend_pizza in friend_paizzas:
	print(friend_pizza)

print('-' * 100)

# 4.12
my_foods = ['pizza', 'falafel', 'carrot cake', 'pizza vegetables',
            'pizza chicken ', 'only pizza']
print('the first list of food :')
for food in my_foods[:3]:
	print(food)

print("\nthe second list of fast food :")
for fast_food in my_foods[-3:]:
	print(fast_food)
print('-' * 100)

# 4.13 buffer ( tuple )
foods = ('rice', 'eggs', 'bread with eggs', 'pasta', 'كرسبي')
for food in foods:
	print(food)

foods =('rice', 'eggs', 'bread with eggs', 'pasta', 'potatoes', 'sweat')
print("\nmodify foods :")
for food in foods:
	print(food)

