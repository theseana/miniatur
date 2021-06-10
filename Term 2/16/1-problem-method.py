text = input('Enter your info: (ex. "name family age")\n')

info = text.split()

template = f"""
Name:   {info[0].title()}, 
Family: {info[1].upper()},
Age:    {info[2]},"""

print(template)