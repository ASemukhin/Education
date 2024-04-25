from Models import *

Users.create(name = 'Alice', Mail = 'Alice@mail.ru', Password = '1234567')
Users.create(name = 'Bob', Mail = 'Bob@gmail.com', Password = 'qwerty')
Users.create(name = 'Nick', Mail = 'Nick@yandex.ru', Password = '1234567')

Task.create(Users.id==1, Exercise == 'Задание_1')
Task.create(Users.id==2, Exercise == 'Задание_2')
Task.create(Users.id==3, Exercise == 'Задание_3')

# #1
# users = Users.get(Users.id == 2)
# users.name = 'Tom'
# users.save()
#
# #2
#
# user = Users.get(Users.Mail == 'Nick@yandex.ru')
# user.delete_instance()
#
# #3
#
# users = Users.select().where(Users.name ** 'A%')
# for user in users:
#      print(user.name)
#
# #4
#
# users = Users.select().where(Users.Mail ** '%gmail.com')
# for user in users:
#      print(user.Mail)

#5 --- Не много не так выполнил, через select не работает, 3 не читает, потому что он удален

# user = Users.get(Users.id == 1)
# print(user.name, user.Mail,user.Password, Task.Exercise)
# user = Users.get(Users.id == 2)
# print(user.name, user.Mail,user.Password, Task.Exercise)
# user = Users.get(Users.id == 3)
# print(user.name, user.Mail,user.Password, Task.Exercise)

#6
# query = (Users
#          .select(Task.Exercise)
#          .join(Task,JOIN.LEFT_OUTER)
#          .dicts()
#          )
# for row in query:
#     print(row)

#7

# user = Users.get(Users.Mail == 'Alice@mail.ru')
# print(user.name, user.Mail,user.Password, Task.Exercise)

#8

query = (Users.select(Users,Task).
         join(Users,Task).dicts())
for row in query:
    print(row)