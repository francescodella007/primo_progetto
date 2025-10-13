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