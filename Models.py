from peewee import *

db = SqliteDatabase('base.db')


class Users(Model):
    name = CharField()
    Mail = TextField()
    Password = TextField()

    class Meta:
        database = db

class Task(Model):
    user = ForeignKeyField(Users, backref='posts')
    Exercise = TextField()

    class Meta:
        database = db

if __name__ == '__main__':
    db.create_tables([Users,Task])

