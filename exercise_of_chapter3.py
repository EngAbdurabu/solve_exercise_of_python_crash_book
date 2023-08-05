# 3.1
names = ['Ahamed', 'Ali', 'Majid', 'Salem', 'Omer']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])

# 3.2
massage = f'this is student lase then my {names[0].upper()} by two year '
massage2 = f'this is student lase then my {names[1].upper()} by two year '
massage1 = f'this is student lase then my {names[2].upper()} by two year '
massage3 = f'this is my close friend : {names[3].upper()}  '
massage4 = f'this is student: {names[4].upper()}is with my in my final project '
print(massage.title())
print(massage1.title())
print(massage2.title())
print(massage3.title())
print(massage3.title())

# 3.3
cars = ['Honda', 'Ford', 'Toyota', 'Mercedes', 'tesal']
print(f'I like the car of {cars[2].upper()} company ')
print(f'I would like to have {cars[-1].upper()}because it is electrical car type ')
print(f'I think the {cars[-2].upper()} is the professional car')
print('++'*50)

# 3.4
deceased_people = ['Safe', 'Ahmed', 'Ali']
print(f'hi {deceased_people[0].title()} I would like to invite you to my dinner ')
print(f'hi {deceased_people[1].title()} I would like to invite you to my dinner ')
print(f'hi {deceased_people[2].title()} I would like to invite you to my dinner')
print('++'*50)

# 3.5
life_people = ['Salem', 'Ali', 'Hussain']
print(f'hi {life_people[0].title()} I would like to invite you to my dinner ')
print(f'hi {life_people[1].title()} I would like to invite you to my dinner ')
print(f'hi {life_people[2].title()} I would like to invite you to my dinner')
print('++'*50)

# 3.6
life_people.insert(0, 'Majid')
life_people.insert(2, 'Mohammed')
life_people.append('Saleh')
print(life_people)
print(f'my dear {life_people[0].title()}, I would like to invite you to my dinner ')
print(f'my dear {life_people[1].title()}, I would like to invite you to my dinner ')
print(f'my dear {life_people[2].title()}, I would like to invite you to my dinner')
print(f'my dear  {life_people[3].title()}, I would like to invite you to my dinner ')
print(f'my dear {life_people[4].title()}, I would like to invite you to my dinner ')
print(f'my dear {life_people[5].title()}, I would like to invite you to my dinner')
print('++'*50)

# 3.7
print(f'I can invite only two people for dinner I sorry : {life_people}')
print(f" I am sorry I can't invite you to dinner to night {life_people.pop()}")
print(f" I am sorry I can't invite you to dinner to night {life_people.pop()}")
print(f" I am sorry I can't invite you to dinner to night {life_people.pop()}")
print(f" I am sorry I can't invite you to dinner to night {life_people.pop()}")
print(life_people)
print(f"my dear {life_people[0].upper()}, we are still in our invite to night ")
print(f"my dear {life_people[1].upper()}, we are still in our invite to night ")
del life_people[0]
del life_people[0]
print(life_people)
print('=='*100)

# 3.8
places = ['jaben', 'inglend', 'sau', 'egiabt', 'moroco']
print(places)

print('\nthe order :', sorted(places))
print('\nthe original list :', places)
print('use reverse temp', sorted(places, reverse=True))
# show in sorted temporarily
print('the list original :', places)
places.reverse()
print('the list after reverse :', places)
places.reverse()
print('the list after reverse again :', places)
places.sort()
print('the list after sort permanently : ', places)
places.sort(reverse=True)
print('the list after sort reverse permanently :', places)
print('=='* 70)

# 3.9
list = ['Salem', 'Ali', 'Hussain','Safe', 'Ahmed', 'Ali']
print("the people I inviting to dinner is : ", len(list))
print('=='* 70)

# 3.10 use all method in this chapter 
computeres = ['asus', 'dell', 'hp', 'toshaipa', 'esear', 'lenovo']
computeres.append('login')
print('adding using append:', computeres)
computeres.insert(2, 'apple')
print('adding using insert: ', computeres)
computeres.remove('toshaipa')
print('remove using remove :', computeres)
del computeres[4]
print('remove using del :', computeres)
more_uses = computeres.pop()
print('this using pop :', more_uses, '\n', 'this after pop :', computeres)
temp = sorted(computeres)
print('temp sort:', temp, '\nthe original:', computeres)
computeres.sort()
print('permi sort :', computeres)
computeres.reverse()
print('reverse the list :', computeres)
print(len(computeres))




