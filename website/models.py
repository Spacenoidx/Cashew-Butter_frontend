from enum import unique
from os import name
from peewee import *
import datetime
from flask_login import UserMixin

# The database for the entire project is created here. It needs to be created before
# the models can be created. However, it does NOT need to be connected to here. This is
# simply a staging ground.

db = SqliteDatabase("test.db")


# Basemodel from PeeWee helps us establish our own tables.

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel, UserMixin):
    id = PrimaryKeyField()
    email = CharField(unique=True)
    username = CharField(unique = True)
    password = CharField()
    cash_on_hand = IntegerField (default = 150000)

class Horse(BaseModel):
    name = CharField(unique=True)
    gender = CharField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    
#Only drive the program if we run from this module.
    
if __name__ == "__main__":
    db.connect()
    print("Running from models.py ...")
    User.drop_table()
    Horse.drop_table()
