from django.shortcuts import render
import random
# Create your views here.
def index(request):
    return render(request, "prova_pratica_0/index.html")

def somma(request):
    s1 = random.randint(1,10)
    s2 = random.randint(1,10)
    context = {
        'var1':s1,
        'var2':s2,
        'somma': s1 + s2
    }
    somma = context["var1"]+context["var2"]
    return render(request, "prova_pratica_0/somma.html", context)

def media(request):
    lista = []
    s = 0
    for i in range (0,30):
        var = random.randint(1,10)
        s += var
        lista.append(var)

    context = {
        "var": lista,
        "somma": s,
        'divisione': s / 30
    }
    
    return render (request, "prova_pratica_0/media.html", context) 