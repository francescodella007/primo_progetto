from django.shortcuts import render

# Dizionario con studenti, materie, voti e assenze
dizionario = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}

# VIEW A – Visualizza elenco materie
def view_a(request):
    materie = ["Matematica", "Italiano", "Inglese", "Storia", "Geografia"]
    context = {
        "materie": materie
    }
    return render(request, 'listamaterie.html', context)

# VIEW B – Visualizza tutti i voti
def view_b(request):
    context = {
        "voti": dizionario
    }
    return render(request, 'maxMinVoti.html', context)

# VIEW C – Media dei voti di ciascuno studente
def view_c(request):
    medie = {}
    for studente, dati in dizionario.items():
        somma = 0
        conta = 0
        for materia, voto, assenze in dati:
            somma = somma + voto
            conta = conta + 1
        media = somma / conta
        medie[studente] = media

    context = {
        "medie": medie
    }
    return render(request, 'mediastudenti.html', context)

# VIEW D – Voto massimo e minimo per ogni studente
def view_d(request):
    risultati = {}
    for studente, dati in dizionario.items():
        voto_max = -1
        voto_min = 12
        materia_max = ""
        materia_min = ""
        for materia, voto, assenze in dati:
            if voto > voto_max:
                voto_max = voto
                materia_max = materia
            if voto < voto_min:
                voto_min = voto
                materia_min = materia
        risultati[studente] = {
            "voto_massimo": (materia_max, voto_max),
            "voto_minimo": (materia_min, voto_min)
        }
    context = {
        "risultati": risultati
    }
    return render(request, 'votistudenti.html', context)