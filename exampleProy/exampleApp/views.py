from django.shortcuts import render
from django.http import JsonResponse

def exampleView(request):
    example={
    'id':1,
    'name':'juandiego',
    'score':'28'
    }
    return JsonResponse(example)

