# 
# import time


# for hour in range(24):
#     for minut in range(60):
#         for second in range(60):
#             print(f'{hour}:{minut}: {second}')
#             time.sleep(0.1)
 








# nums = [1,2,3,4,5,6,7,8,9,0,10,3,7,9]
# s = set(nums)

# nums_t = []
# for i in s:
#     if nums.count(i) > 1:
#         a = (i,nums.count(i))
#         nums_t.append(a)
# print(nums_t)




#  s = set(a)

#  if len(a != len(s):
    
#     print('ЗНАЧЕНИЯ ПОВТОРЯЮТСЯ')
# else:
#     print('они уникальны')

# print(s)
# print(a
from pprint import pprint

users = {
    '1234567890':{
        'name': 'Asan',
        'last_name':'Usenov',
        'data':2000,
        'gender': 'm',
        'status': False,
        'ID': 'AK47'
        },
    '0987654321':{
        'name': 'Arsen',
        'last_name':'Asanov',
        'data':2003,
        'gender': 'm',
        'status': False,
        'ID': 'AK43'
        }
}

users['1111122222'] = {
        'name': 'Alina',
        'last_name':'Asanova',
        'data':1996,
        'gender': 'f',
        'status': True,
        'ID': 'Asanova96'
}

inn = input('Введите инн: ')
name = input('Введите имя: ')
last_name = input('Введите фамилию: ')
data = input('Введите дату рождения: ')
gender = input('Введите пол: ')
status = input('Введите статус: ')
ID = input('Введите ID: ')

users[inn] = {
'name': name,
'last_name':last_name,
'data':data,
'gender': gender,
'status': status,
'ID': ID
}

pprint(users)
pprint(users[inn])