a='Python\bprogramming'
print(a)


a='Python\rabc'
print(a)

a='python\'s'
print(a)


a='python'
print(a.upper())

a='python'
print(a.lower())

a='python program'
print(a.capitalize())

a='python program'
print=(a.title())

a='python'
print(a.center(9,'*'))

a='python'
print(a.ljust(10,'*'))

a='python'
print(a.index('p'))

a='python'
print(a.find('p'))

a='python'
print(a.rindex('p'))

a='python'
print(a.rfind('p'))

a='pythonp'
b=a.rfind('p')
c=b-len(a)
print(c)

a='python'
print(a.replace('p','z'))


a='python'
b=a.maketrans('p','z')
print(a.translate(b))

a='python'
b=a.maketrans('pxk','wxk')
print(b)