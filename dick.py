# problem 5
# a = []
# b = []
# for i in range(1,10):
#         a.append(i)
#         b.append(i)
# b.reverse()    
# a.extend(b)
# print(*a, sep=', ')
# set1 = {'arsen','mars','bob','beka','almaz'} #показывает недостающие элементы 
# set2 = {'arsen','akyl','bob','abai','almaz'}
# set3 = set1.difference(set2)
# print(set3)

# a = {1,2,3}
# b = {4,5,6}
# a.update(b)
# a.remove(1)
# print(i)


# a = {1,2,3,4,5,}
# b = {1,2,3,6,8,9}
# c = a.intersection(b)
# print(c)

a = {
    'number':[4,7,8]
}


for value in a.values():
    print(value[2])