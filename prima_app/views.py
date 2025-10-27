from django.shortcuts import render
#una funzione usata per inviare al client una pagina html. 
# In questo caso passiamo la pagina creata in precedenza. 
# Ricordarsi il return
def homepage (request):
    return render (request, "prima_app/homepage.html")

def welcome (request):
    return render (request, "prima_app/welcome.html")

def lista (request):
    return render (request, "prima_app/lista.html")

def chi_siamo (request):
    return render (request, "prima_app/chi_siamo.html")

def variabili(request):
    context = {
        'var1':'Prima variabile',
        'var2':'Seconda variabile',
        'var3':'Terza variabile'
    }
    return render(request, "prima_app/variabili.html",context)

def index (request):
    return render (request, "prima_app/index.html")