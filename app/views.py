from django.shortcuts import render
from app.forms  import * 
from django.http import HttpResponse
# Create your views here.
def insert_topic(request): 
    ETFO=TopicForm()
    d={'ETFO':ETFO}  

    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid(): 
            TFDO.save()
            return HttpResponse('insert_topic is created')
    return render(request,'insert_topic.html',d) 

def insert_webpage(request): 
    EWFO=WebpageForm()
    d={'EWFO':EWFO}  

    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid(): 
            WFDO.save()
            return HttpResponse('insert_webpage is created')
    return render(request,'insert_webpage.html',d) 

def insert_accessrecord(request):  
    EARFO=AccessRecordForm()
    d={'EARFO':EARFO}  

    if request.method=='POST':
        ARFDO=AccessRecordForm(request.POST)
        if ARFDO.is_valid(): 
            ARFDO.save()
            return HttpResponse('insert_accessrecord is created')



    return render(request,'insert_accessrecord.html',d)
