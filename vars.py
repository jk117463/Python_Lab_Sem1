a = 10
b = 20
c = a + b
print(c)
print('a: {}'.format(a))
print('b: {}'.format(b))
print('c: {}'.format(c))
print(type(c)) # Class Int

x = 10.123456789
y = 20.123456789
z = x + y
print('x: {}'.format(x))
print('y: {}'.format(y))
print('z: {}'.format(z))
print(type(z)) # Class float

#Lab 4
# Python assigning datatype based on value
d = 2222222222222222222222222222222222222222222.0
print(type(d))
e = 2222222222222222222222222222222222222222222
print(type(e))
f =0.00000000000000000001234567324324324324237667
print(f)

bb = 0b101
print(bb)
xx = 0x101
print(xx)
xx = 0xff
print(xx)

a1 = 1349
b1 = 353
c1 = a1 / b1
# No conversion for str. This will fail. print('c1: {}'.str(c1))
print('c1: {}'.format(c1))
c2 = int(c1)
print('c2: {}'.format(c2))
c3 = round(c1)
print('c3: {}'.format(c3))

s = '123.456'
print('type of s: {}'.format(type(s))) # Typecaseting it as string and printing allow to avoid exponential notation


# Automatic checking on possible typecasting
s1 = 'f123.456'
s2 = '123'
print(s1.isdigit())
print(s2.isdigit())
print(s2.isalnum())
print(s2.isalpha())

# Changing bases
s1 = '101'
#interpret as hexadecimal
print(int(s1, 16))
#interpret as binary
print(int(s1, 2))