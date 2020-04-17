"""
x = 'Ross\nTaylor'
print(x)
"""
first_name = 'Ross'
last_name = 'Taylor'
name = (first_name, last_name)
print(name)
print(type(name))
print(name[0])   # tuple supports indexing
print('Hello {} {}! You just delved into python.'.format(first_name,last_name))
