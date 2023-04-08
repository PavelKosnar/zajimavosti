import random

def hash_by_division(k, m):
    return abs(k % m)

def store_it(item, list, length):
    index = hash_by_division(hash(item), length)
    if list[index] == None:
        list[index] = item
    elif type(list[index]) == type([]):
        list[index].append(item)
    else:
        list[index] = [list[index], item]
    return list

def find_it(item, list, length):
    index = hash_by_division(hash(item), length)
    if list[index] == None:
        return False
    return list[index] == item or item in list[index]

delka = 13
slova = [random.randint(0, 10000) for _ in range(5000)]
neco = [None for _ in range(delka)]
for i in slova:
    neco = store_it(i, neco, delka)
print(*(f'{indx}, {i}\n' for indx, i in enumerate(neco) if i != None))
print('----------------------')
for i in range(5000, 15000):
    print(find_it(i, neco, delka), i)
