from django.db import models
import ctypes

# Create your models here.
class Chat(models.Model):
    name= models.TextField(default='unknown')
    msg= models.TextField(default='')
    sendTime= models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "chat"


class Gamming():
    def __init__(self, creator_id, p1_name) -> None:
        self.room_id= self
        self.openingStatus= False
        self.creator_id= creator_id
        self.p1_id= creator_id
        self.p1_name= p1_name
        self.p2_id= ''
        self.p2_name= ''
        self.position= {"p1":[15,0], "p2":[85,0], "ball":[15,60]}
        self.speed= {'p1':[0,0], 'p2':[0,0], 'ball':[0,0]}
        self.scores= {'p1':0, 'p2':0}
    


class GammingRooms():
    rooms= []
    emptyRoomChecking= None
    
    def newRoom(self, creator_id, p1_name):
        newRoom= Gamming(creator_id, p1_name)
        newRoom.room_id= id(newRoom)
        self.rooms.append(newRoom)
        return id(newRoom)
    @staticmethod
    def getRoom(self, room_id):
        return  ctypes.cast(room_id, ctypes.py_object).value
    @staticmethod
    def getRooms(self, col='*'):
        if col == '*':
            return  self.rooms
        return [getattr(roomObj, col,'') for roomObj in self.rooms]
    @staticmethod
    def delRoom(self, room_id):
        if room_id in self.rooms:
            self.rooms.remove(self.getRoom(room_id))


textColor= {"default":"\033[37m", "gray":"\033[90m", "red":"\033[31m", "green":"\033[32m", "blue":"\033[34m", "yello":"\033[33m"}

class memoryObj():
    content= {}
memoryDict= {}