from django.shortcuts import render

#add2018.08.19 start
from django.http import HttpResponse
#add2018.08.19 end

# Create your views here.
#add2018.08.19 start
def hello(request):
    return HttpResponse('こんにちは')
#add2018.08.19 end
#add2018.08.25 start
def card(request):
    return render(request,'card.html')
def welcome(request):
    class person(object):
        def __init__(self, name, sex="famale")
            self.name = name
            self.sex = sex 
            
    me = person("みずはら","Male")
    dictionary = {"person" : me}
    return render(request,'name.html',dictionary)
#add2018.08.25 end
