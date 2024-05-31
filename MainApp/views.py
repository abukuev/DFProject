from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def Home(request):

    text = "</h1>HELLO</h1>"
    context={'name':'Алексей', 'surname':'Букуев'}
    
    return render(request,'index.html',context)
