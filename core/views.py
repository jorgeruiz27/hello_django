from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))

def soma(reuqest, num1, num2):
    soma = num1 + num2
    return HttpResponse('Soma obtida de {} + {} é igua a {}'.format(num1,num2,soma))

def sub(reuqest, num1, num2):
    sub = num1 - num2
    return HttpResponse('Subtracao obtida de {} - {} é igua a {}'.format(num1,num2,sub))

def mult(reuqest, num1, num2):
    mult = num1 * num2
    return HttpResponse('Multiplicacao obtida de {} * {} é igua a {}'.format(num1,num2,mult))

def div(reuqest, num1, num2):
    div = num1 / num2
    return HttpResponse('Divisao obtida de {} / {} é igua a {}'.format(num1,num2,div))