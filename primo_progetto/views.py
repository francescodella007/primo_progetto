from django.shortcuts import render
#una funzione usata per inviare al client una pagina html. 
# In questo caso passiamo la pagina creata in precedenza. 
# Ricordarsi il return
def base (request):
    return render (request, "base.html")