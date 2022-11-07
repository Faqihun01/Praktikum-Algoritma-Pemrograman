a = 4
b = 2
# lebih besar dari >
print('========== lebih besar dari (>)')
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)
print("\n")

# kurang dari <
print('========== kurang dari (<)')
hasil = a < 3
print(a,'<',3,'=',hasil)
hasil = b < 3
print(b,'<',3,'=',hasil)
hasil = b < 2
print(b,'<',2,'=',hasil)
print("\n")

# lebih dari sama dengan >=
print('========== lebih dari sama dengan(>=)')
hasil = a >= 3
print(a,'>=',3,'=',hasil)
hasil = b >= 3
print(b,'>=',3,'=',hasil)
hasil = b >= 2
print(b,'>=',2,'=',hasil)
print("\n")

#kurang dari sama dengan <=
print('======== kurang dari sama dengan(<=)')
hasil = a <= 3
print(a,'<=',3,'=',hasil)
hasil = b <= 3
print(b,'<=',2,'=',hasil)
hasil = b <= 2
print(b,'<=',2,'=',hasil)
print("\n")

# sama dengan (==)
print('======== sama dengan(==)')
hasil = a == 4
print(a,'==',4,'=',hasil)
hasil = b == 4
print(b,'==',4,'=',hasil)
print("\n")

# tidak sama dengan (!=)
print('======== tidak sama dengan(!=)')
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)
print("\n")

# 'is' sebagai komparasi object identity
print('======== object identity(is)')
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)
print("\n")

x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)
print("\n")

print('======== object identity(is not)')
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is y =',hasil)
print("\n")

x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is not y
print('x is y =',hasil)



