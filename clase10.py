from itertools import pairwise


numbers = {1: 'uno', 2: 'dos', 3: 'tres'}
print(numbers[2])  # Output: 'dos'
information = {'name': 'Leonardo',
               'age': 41, 
               'city': 'Colombia'} 
print(information['name'])  # Output: 'Leonardo'
print(information['age'])   # Output: 41
print(information['city'])  # Output: 'Colombia'

claves = information.keys()
print(claves)  # Output: dict_keys(['name', 'age', 'city'])
print(type(claves))  # Output: <class 'dict_keys'>
values = information.values()
print(values)  # Output: dict_values(['Leonardo', 41, 'Colombia'])
pairs = information.items()
print(pairs)  # Output: dict_items([('name', 'Leonardo'), ('age', 41), ('city', 'Colombia')])
print(type(pairs))  # Output: <class 'dict_items'>  

contacts = {'Leonardo':{'age': 41,
               'city': 'Colombia'},
               'Maria':{'age': 30,
                      'city': 'Argentina'}}
print(contacts['Leonardo'])  # Output: {'age': 41, 'city': 'Colombia'}
print(contacts['Leonardo']['age'])  # Output: 41
print(contacts['Maria']['city'])  # Output: 'Argentina' 
