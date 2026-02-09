from django.shortcuts import get_object_or_404, render
import datetime
from .models import Articolo, Giornalista
from django.db.models import Q

# Create your views here.
def home (request):
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context = {"articoli": articoli, "giornalisti": giornalisti}
    print(context)
    return render (request, "news/homepage.html", context)

def articoloDetailView(request, pk):
    #articolo = Articolo.objects.get(pk=pk)
    articolo = get_object_or_404(Articolo, pk=pk)
    context = {"articolo": articolo}
    return render(request, "articolo_detail.html", context)

def query(request):
    #filtro per cognome del giornalista
    articoli_cognome = Articolo.objects.filter(giornalista__cognome ="rossi")
    
    #numero totale di articoli
    numero_totale_articoli = Articolo.objects.count() #totale

    #conta il numero di articoli scritti da un specifico giornalista
    giornalista_1 = Giornalista.objects.get(id=3)
    numero_Articoli_giornalista1 = Articolo.objects.filter(giornalista=giornalista_1).count()

    #tutti gli articoli che non hanno visualizzazioni
    articoli_senza_visualizzazioni = Articolo.objects.filter(visualizzazioni=0)

    #articolo più visualizzato
    articolo_piu_visualizzato = Articolo.objects.order_by("-visualizzazioni").first()

    #tutti i giornalisti dopo una certa data
    giornalisti_dopo_data = Giornalista.objects.filter(anno_di_nascita__gt="1990-01-01")

    #articoli pubblicati in una data precisa
    articoli_data_precisa = Articolo.objects.filter(data="2023-01-01")

    #articoli pubblicati in un intervallo di date
    articoli_intervallo_date = Articolo.objects.filter(data__range=["2023-01-01", "2023-12-31"])

    #articoli scritti da giornalisti nati prima del 1980
    articoli_giornalisti_pre1980 = Articolo.objects.filter(giornalista__anno_di_nascita__lt="1980-01-01")

    #giornalista più giovane
    giornalista_piu_giovane = Giornalista.objects.order_by("-anno_di_nascita").first()

    #giornalista più anziano
    giornalista_piu_anziano = Giornalista.objects.order_by("anno_di_nascita").first()

    #ultimi 5 articoli pubblicati
    ultimi_5_articoli = Articolo.objects.order_by("-data")[:5]

    #articoli con un numero minimo di visualizzazioni
    articoli_minimo_visualizzazioni = Articolo.objects.filter(visualizzazioni__gte=100)

    #filtro nel titolo che contiene una parola specifica
    articoli_con_parola_titolo = Articolo.objects.filter(titolo__icontains="importante")
    
    #PASSO 19
    #articoli pubblicati in un mese di un anno specifico
    articoli_mese_anno = Articolo.objects.filter(data__month=1, data__year=2023)

    #giornalisti con almeno un articolo con più di 100 visualizzazioni
    giornalisti_con_articoli_popolari = Giornalista.objects.filter(articoli__visualizzazioni__gte=100).distinct()

    data = datetime.date(1990, 1, 1)
    visualizzazioni = 50
    #scrivi quali articoli vengono selezionati con l'AND
    articoli_con_AND = Articolo.objects.filter(giornalista__anno_di_nascita__gt=data, visualizzazioni__gte=visualizzazioni)

    #scrivi quali articoli vengono selezionati con l'OR
    articoli_con_OR = Articolo.objects.filter(Q(giornalista__anno_di_nascita__gt = data) | Q(visualizzazioni__lte=visualizzazioni))

    #scrivi quali articoli vengono selezionati con il NOT
    articoli_con_NOT = Articolo.objects.filter(~Q(giornalista__anno_di_nascita__lt = data))

    #oppure con il metodo exclude
    #articoli_con_NOT = Articolo.objects.exclude(giornalista__anno_di_nascita__lt = data)

    context = {
        "articoli_cognome": articoli_cognome,
        "numero_totale_articoli": numero_totale_articoli,
        "numero_Articoli_giornalista1": numero_Articoli_giornalista1,
        "articoli_senza_visualizzazioni": articoli_senza_visualizzazioni,
        "articolo_piu_visualizzato": articolo_piu_visualizzato,
        "giornalisti_dopo_data": giornalisti_dopo_data,
        "articoli_data_precisa": articoli_data_precisa,
        "articoli_intervallo_date": articoli_intervallo_date,
        "articoli_giornalisti_pre1980": articoli_giornalisti_pre1980,
        "giornalista_piu_giovane": giornalista_piu_giovane,
        "giornalista_piu_anziano": giornalista_piu_anziano,
        "ultimi_5_articoli": ultimi_5_articoli,
        "articoli_minimo_visualizzazioni": articoli_minimo_visualizzazioni,
        "articoli_con_parola_titolo": articoli_con_parola_titolo,
        "articoli_mese_anno": articoli_mese_anno,
        "giornalisti_con_articoli_popolari": giornalisti_con_articoli_popolari,
        "articoli_con_AND": articoli_con_AND,
        "articoli_con_OR": articoli_con_OR,
        "articoli_con_NOT": articoli_con_NOT,
    }
    return render (request, "news/query.html", context)

def lista_articoli (request):
    articoli = Articolo.objects.all()
    context = {"articoli": articoli}
    return render (request, "lista_articoli.html", context)

def giornalistaDetailView(request, pk=None):
    giornalisti = Giornalista.objects.all()
    context = {"giornalisti": giornalisti}
    return render(request, "giornalista_detail.html", context)