print('-----------------------------------------------------')
# LAMBDA
print('LAMBDA:\n')
print((lambda x, y: x+y)(1, 2))
# The same as:


def add(x, y):
    return x+y


print(add(1, 2))
print('-----------------------------------------------------')

# F-STRING FORMAT
print('F-STRING FORMAT:\n')
text = 'FUN'
num = 1000000
print(f'{text}')
print(f'{text:.<20}')
print(f'{text:.>20}')
print(f'{text:.^20}')
print(f'{num}')
print(f'{num:_}')
print('-----------------------------------------------------')

# VARIABLE SWAP
print('VARIABLE SWAP:\n')
a = 5
b = 10
print(a, b)
a, b = b, a
print(a, b)
print('-----------------------------------------------------')

# LIST FOR LOOP IN ONE LINE
print('LIST FOR LOOP IN ONE LINE:\n')
numbers = [i*i for i in range(10) if i % 2 == 0]
print(numbers)
print('-----------------------------------------------------')

# IF-ELSE IN ONE LINE
print('IF-ELSE IN ONE LINE:\n')
num = 3
var = 42 if num > 2 else 99
print(var)
num = 2
var = 42 if num > 2 else 99
print(var)
print('-----------------------------------------------------')

# PRINT LIST VALUES
print('PRINT LIST VALUES:\n')
numbers = [0, 1, 2, 3, 4, 5]
print(*numbers)
print('Done')
print('-----------------------------------------------------')

# REVERSE A LIST OR A STRING
print('REVERSE A LIST OR A STRING:\n')
numbers = numbers[::-1]
print(numbers)
text = 'CRAZY'
text = text[::-1]
print(text)
text = 'LEVEL'
print(text == text[::-1])
print('-----------------------------------------------------')

# STRING TO LIST
print('STRING TO LIST:\n')
numbers = '1 2 3 4 5'
str_to_list = numbers.split()
print(str_to_list)
str_to_int_list = list(map(int, numbers.split()))
print(str_to_int_list)
print('-----------------------------------------------------')

# FILE TO LIST (also removes white space)
print('FILE TO LIST:\n')
file_to_list = [line.strip() for line in open('file_to_list.txt', 'r')]
print(file_to_list)
print('-----------------------------------------------------')
