from SerieCard import SerieCard


class Episode(SerieCard):

    compteur = 1000000

    def __init__(self):
        SerieCard.__init__(self)
        self.serie = None
        self.seasons = None
        self.id = Episode.compteur
        Episode.compteur =+1



