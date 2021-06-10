# capitalize
name = 'maedeh ashouri'
name = name.capitalize()
print(name)
# count
name = 'man maedeh ashouri hastam'
number = name.count('a')
print(number)

# endswith
name = 'man maedeh ashouri hastam'
status = name.endswith('ri')
print(status)

# find
name = 'man maedeh ashouri hastam'
number = name.find('e')
print(number)

# index
name = 'man maedeh ashouri hastam'
number = name.find('e')
print(number)

# isalnum
name = 'man1maedeh2ashouri3hastam'
status = name.isalnum()
print(status)

# isalpha
name = 'manmaedehashourihastam'
status = name.isalpha()
print(status)
# isdecimal
# isdigit
# isnumeric

# islower
name = 'manmaedehaShourihastam'
status = name.islower()
print(status)

# isspace
name = '     '
status = name.isspace()
print(status)

# istitle
name = 'Maedeh Ashouri'
status = name.istitle()
print(status)

# isupper
name = 'MAEDEH ASHOURI'
status = name.isupper()
print(status)

# join
words = ['man', 'maedeh', 'ashouri', 'hastam']
print(" ".join(words))

# lower
name = 'MAEDEH ASHOURI'
name = name.lower()
print(name)

# replace جاگذاری
name = 'MAEDEH ASHOURI'
name = name.replace('M', '^^')
print(name)

# split برش
name = 'MAEDEH ASHOURI KHAHAM BUD'
name = name.split('H')
print(name)

# startswith
name = 'man maedeh ashouri hastam'
status = name.startswith('man')
print(status)

# strip
name = '#@$@#$@#$MAEDEH@#$@#$@#$@#$'
name = name.strip('#$@')
print(name)

# swapcase
name = 'MAEDEH AsHOURi TaDa!'
name = name.swapcase()
print(name)

# title
name = 'man maedeh ashouri hastam'
name = name.title()
print(name)

# upper

# zfill
number = '13'
number = number.zfill(4)
print(number)