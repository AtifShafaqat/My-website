from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data={
        'title' : 'you tube',
        'bdata': 'welcome my website',
        'clist': ['php','java','django'],
        'number':[10,20,30,40,50],
        'Student_detail':[
            {'name':'ali','phone':30394304903},
            {'name':'atif','phone':3084906432}
        ]
    }
    
    return render(request,"index.html",data)

def aboutus(request):
    return HttpResponse('<b>welcome to my first mywebsite</b>')

# def course(request):
#     return HttpResponse('welcome to my first33 mywebsite')

# def courseDetails(request,courseid):
#     return HttpResponse(courseid)
