#code 1
#print('Hello there!')

#code 2
#print('My name is:')
#print('Lukasz')

#code 3
#print('I am', 20, 'years old')

#city = 'Wroclaw'
#today = 29
#print('Today is', today, 'in', city)
'''
my_age = '20'
your_age = '22'
print(my_age + your_age)

city = 'Wroclaw'
country = 'Poland'
europe = 'Europe'

print(city, 'is in', country,)
print(country, 'is in', europe)

initial = 'left'
position = initial
initial = 'right'
print(position)

your_name = 'Lukasz'
print('First letter:', your_name[0])
print('Second letter:', your_name[1])
print('Third letter:', your_name[2])
print('Fourth letter:', your_name[3])
print('Fifth letter:', your_name[4])
print('Sixth letter:', your_name[5])

print(your_name[0:4])

my_string = 'Yoland'
my_string = 'P' + my_string[1:]
print(my_string)
'''

'''
#code 1
my_string = 'It5ly'
print(my_string)

#code 2
string_1 = 'I live in Italy'
current_country = 'Poland'
my_string = string_1[0:10] + current_country
print(my_string)
'''

#integer_1 = 1
#integer_2 = '10a'
#print(integer_1 + int(integer_2))
'''
t = 1
print(type(t))

t = 1.0
print(type(t))

t = 5/2
print(type(t))

number = 500
print(str(number)[0])
'''
'''
eur = 4.3
euro_in_my_pocket = 100
pln_in_my_pocket = euro_in_my_pocket * eur
print(pln_in_my_pocket)
'''

'''
empty_list = []
print(type(empty_list))

my_first_list = [1,2,3,4,5]
a_mixed_list = [1,2,'Ciao']
new_list = my_first_list + a_mixed_list
print(new_list)

print(my_first_list[-1])

print(my_first_list[::-1]) #reversing list

countries = ['Poland', 'Italy', 'USA', 'Germany']
for country in countries:
	print(country)

country = 'Poland'
for l in enumerate(country):
	print(l)

for i, v in enumerate(country):
	print(i, v)

for l in range(len(country)):
	print(l, country[l])
'''

'''
initial = ['left']
position = initial
initial = ['right']
print(position)

initial = ['left']
position = initial
initial[0] = 'right'
print(position)
'''

dicty = {'key': 'value', 'key1': 'value1'}
print(dicty['key'])
print(dicty)

dicty[1] = 'ValueFrom1'
dicty['ssss'] = 'valueFromssss'

print(dicty)

for k in dicty:
	print('Key:', k, 'Value:', dicty[k])

#dir(dicty) shows a list of available methods

for k, v in dicty.items():
	print('Key:', k, 'Value:', v)