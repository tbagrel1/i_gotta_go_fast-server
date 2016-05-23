from django.shortcuts import HttpResponse
from app1.models import Score

def _viewScores(request):

    pseudo_cur = request.GET.get('pseudo', None)
    date_cur = request.GET.get('date', None)
    heure_cur = request.GET.get('heure', None)

    try:
        db = list(Score.objects.order_by('-score'))
    except:
        db = None
    if db:
        c = """<html lang="fr">
    <head>
        <meta charset="UTF-8" />
        <style>
            *
            {
                font-family: "Comic sans MS", Verdana, sans-serif;
                font-size: 13px;
            }

            #normal
            {

            }

            #best
            {
                background-color: yellow;
            }

            #self
            {
                background-color: red;
            }

            #cat
            {
                background-color: gray;
            }
        </style>

        <title>Scores IGGF</title>
    </head>

    <body>
        <table>
            <tr>
                <td>ID</td>
                <td>Pseudo</td>
                <td>Score</td>
                <td>Caractères par minute</td>
                <td>Mots par minute</td>
                <td>Temps de jeu</td>
                <td>Date</td>
                <td>Heure</td>
                <td>Texte choisi</td>
            </tr>
"""

        pas_encore_trouve_best = True

        for elt in db:
            type_ligne = ""

            if str(elt.pseudo)[0] == "#":
                type_ligne = "cat"
            elif pas_encore_trouve_best:
                type_ligne = "best"
                pas_encore_trouve_best = False
            elif (str(elt.pseudo) == pseudo_cur and
                  str(elt.date) == date_cur and
                  str(elt.heure) == heure_cur):
                type_ligne = "self"
            else:
                type_ligne = "normal"

                c += """            <tr id={}>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
            </tr>
"""\
                .format(type_ligne,
                        str(elt.id),
                        str(elt.pseudo),
                        str(elt.score),
                        str(elt.cpm),
                        str(elt.mpm),
                        str(elt.temps),
                        str(elt.date),
                        str(elt.heure),
                        str(elt.texte_mode_enh))
        c += """        </table>
    </body>
</html>"""

    else:
        c = "ERROR"

    return HttpResponse(c)
