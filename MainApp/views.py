from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def home(request):

    text = "</h1>HELLO</h1>"
    context={'name':'Алексей', 'surname':'Букуев'}

    return render(request,'index.html',context)



def items(request):
    pass