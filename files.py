# with open('users.txt','a') as f:
#     login = input('введите логин:')
#     password1 = input('введите пароль:')
#     password2 = input('подвердите пароль:')
# while password1!=password2 or len(password1) <=6:
#         password1 = input('пароль не может быть меньше 6 цифр: ')
#         password2 = input('подвердите пароль:') 
        
# f.write('login:{login} password1:{password1}\n')
# print('успешно')

a = [1, 1, 2, 3, 13, 13, 13, 13, 13, 13, 13, 13, 13, 5, 8, 13, 21, 34,1,55, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 1313, 13, 13, 13, 13, 13, 89]
# len(a)
# print(a.count(13))
# print(len(a))

#3

# users = []
# login = input('Введите логин: ')
# password = input('Введите пароль: ')

# users.update
#     user{
#     'login':login,
#     'password':password
#     }

# login = input('Введите ваш логин: ')
# password = input('Введите ваш пароль: ')
# if login in users:
#     if password == users['login']['password']:
#         print('Добро пожаловать')
#     else:
#         print('не правильный логин или пароль')

#2.1

# dict1 = {'a': 5, 'b': 3, 'c': 8, 'd': 14}
# i = dict1
# if i % 3 == 0:
#     print('Bye')
# elif i % 5 == 0:
#     print('hi')

#2.2
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:
#     if i == 0<4:
#         break
#     print(i)

#2.3



#2.4

# word =  "4729461084"
# joined_word = "+".join(word)
# print(joined_word)
import subprocess
systemInfo = ''
try:
    systemInfo = subprocess.check_output(['uname']).decode('utf-8', errors="backslashreplace").split('\n')
    systemInfo = systemInfo[0]
except :
    pass
if systemInfo == "Linux":
    wifiData = subprocess.check_output(['ls', '/etc/NetworkManager/system-connections']).decode('utf-8', errors="backslashreplace").split('\n')
    print ("Wifi                            Password")
    print ("----------------------------------------")
    for wifiname in wifiData:
        if wifiname != '':
            wifiPass = subprocess.check_output(['sudo','cat', f"/etc/NetworkManager/system-connections/{wifiname}"]).decode('utf-8', errors="backslashreplace").split('\n')
            password=wifiPass[15].strip("psk=");
            print ("{:<30} {:<}".format(wifiname, password))
else:
    wifi = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
    profiles = [i.split(":")[1][1:-1] for i in wifi if "All User Profile" in i]
    for i in profiles:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                print ("{:<30}|  {:<}".format(i, results[0]))
            except :
                print ("{:<30}|  {:<}".format(i, ""))
        except :
            print ("{:<30}|  {:<}".format(i, "ОШИБКА КОДИРОВАНИЯ"))