
class Broadcast() :
    """
    Objet diffusion
    Définit  une diffusion d'un épisode sur une chaine TV pour une date"""
    compteur = 1000000

    def __init__(self) :
        self.date = None
        self.episod = None
        self.tvChain = None
        self.id = Broadcast.compteur
        Broadcast.compteur =+ 1
