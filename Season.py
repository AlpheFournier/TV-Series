from SerieCard import SerieCard

class Season(SerieCard) :

    compteur = 1000000

    def __init__(self):
        SerieCard.__init__(self)
        self.serie = None
        self.list_episods = []
        self.year = None
        self.id = Season.compteur
        Season.compteur =+ 1



