from django.db import models
import sqlite3

# Create your models here.



# orm架構
class Users(models.Model):
    
    name= models.TextField(default='')
    msg= models.TextField(default='')
    sendTime= models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "Users"


# SQL語法
def insert():
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    cursor