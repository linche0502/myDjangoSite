from django.db import models
from datetime import datetime
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
        # self.room_id= self
        self.openingStatus= False
        self.creator_id= creator_id
        self.p1_id= creator_id
        self.p1_name= p1_name
        self.p2_id= ''
        self.p2_name= ''
        self.position= {"p1":[15,0], "p2":[85,0], "ball":[15,60]}
        self.speed= {'p1':[0,0], 'p2':[0,0], 'ball':[0,0]}
        self.scores= {'p1':0, 'p2':0}
        self.lastUpdate= datetime.now()


class GammingRooms():
    # rooms= []
    # rooms.key= creator_id
    rooms= {}
    emptyRoomChecking= None
    
    def newRoom(self, creator_id, p1_name):
        self.rooms[creator_id]= Gamming(creator_id, p1_name)
        return creator_id
    @staticmethod
    def getCols():
        return [i for i in Gamming.__dict__.keys() if i[:1] != '_']
    @staticmethod
    def getRoom(room_id):
        return GammingRooms.rooms.get('room_id')
    @staticmethod
    def getRooms(col='*', filter={}):
        # 刪除閒置(斷線)的房間
        rooms, now= GammingRooms.rooms, datetime.now()
        for room in rooms:
            if (now - rooms[room].lastUpdate).second >= 5:
                GammingRooms.delRoom(room)
        if col == '*':
            return  GammingRooms.rooms
        return {room_id:getattr(room_id, col,'') for room_id in GammingRooms.rooms}
    @staticmethod
    # data= {p1_name:'abc', ...}
    def setRoom(room_id, data):
        cols= [i for i in Gamming.__dict__.keys() if i[:1] != '_']
        for col in data:
            if data[col] != GammingRooms.rooms[room_id].get('col') and col in cols:
                setattr(GammingRooms.rooms[room_id], col, data[col])
    @staticmethod
    def delRoom(room_id):
        if room_id in GammingRooms.rooms:
            GammingRooms.rooms.pop(room_id, '')
    
    @staticmethod
    def switchPlayer(self, room_id):
        room= GammingRooms.rooms[room_id]
        if room.p1_id == '' or room.p2_id == '':
            GammingRooms.rooms[room_id].p1_id, GammingRooms.rooms[room_id].p2_id= [GammingRooms.rooms[room_id].p2_id, GammingRooms.rooms[room_id].p1_id]


textColor= {"default":"\033[37m", "gray":"\033[90m", "red":"\033[31m", "green":"\033[32m", "blue":"\033[34m", "yello":"\033[33m"}

class memoryObj():
    content= {}
memoryDict= {}