from SerieCard import SerieCard


class TVSerie(SerieCard) :

    compteur = 1000000

    def __init__(self):
        SerieCard.__init__(self)
        self.seasons = []
        self.episods = []
        self.id = TVSerie.compteur
        TVSerie.compteur =+ 1
# Q : saisons, attributions par objet créé "1,2,3..." ?