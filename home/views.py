from django.shortcuts import render, HttpResponse
from .models import Chat, memoryObj, GammingRooms, memoryDict, textColor
from datetime import datetime
import json, socket, random

# Create your views here.
def home(request):
    if request.POST:
        chatName= request.POST['chatName']
        chatMsg= (request.POST['chatMsg'] or '').strip()
        if chatName and chatMsg:
            Chat.objects.create(name=chatName,msg=chatMsg)
        if chatMsg == "!mod cls":
            Chat.objects.all().delete()
    if request.GET.get('update'):
        data= {}
        for row in Chat.objects.values():
            row_id= row.pop('id')
            data[row_id]= row
            data[row_id]['sendTime']= row.get('sendTime', datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
        return HttpResponse(json.dumps(data))
    if request.GET.get('getNewName'):
        names= set()
        for row in Chat.objects.values():
            names.add(row.get('name'))
        return HttpResponse(json.dumps(list(names)))
    
    ip= socket.gethostbyname(socket.getfqdn(socket.gethostname()))
    
    return render(request, 'home.html', {'ip':ip})


def bikachu(request):
    return render(request, 'bikachu.html')


def connBikachuRooms(request):
    gammingRooms= GammingRooms()
    # hello
    if request.GET.get('get_user_id'):
        while True:
            new_id= random.randint(10000000)
            if new_id not in gammingRooms.getRooms():
                newRoom= gammingRooms.newRoom(new_id, request.GET.get('userName',''))
                return new_id
    if request.GET.get('update'):
        
        return HttpResponse('{}')
    
    return render(request, 'bickchuRoom.html')

def connBikachuGame(request):
    # 前端: 遊戲運算引擎
    room_id= request.GET.get('room_id')
    # request: 各自角色位置, 自身碰撞後球的位置速度
    # response: 對方角色位置,  對方碰撞後球的位置速度
    if request.POST.get('update'):
        
        return HttpResponse('{1:1}')
    if request.POST.get('touch'):
        return HttpResponse('{}')
    
    return render()


def connTest(request):
    if request.POST:
        name= request.POST.get('argName','')
        value= request.POST.get('argValue','')
        thisArgs= {name:value}
        
        memoryObj.content[name]= value
        memoryDict[name]= value
        # obj 紅色
        print(f'{textColor["red"]} obj',
            thisArgs,
            memoryObj.content,
            thisArgs == memoryObj.content,
            textColor["default"])
        # dict 綠色
        print(f'{textColor["green"]} dic',
            thisArgs,
            memoryDict,
            thisArgs == memoryDict,
            textColor["default"])
        return HttpResponse(json.dumps(memoryObj.content))
    
    if request.GET.get('ping'):
        return HttpResponse('')
    
    return render(request, 'connTest.html')

