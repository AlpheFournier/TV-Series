class Person:

    list_of_person = {}
    ident = 1000000

    def __init__(self,id,name,age, nationality, biographie, tv_series_actor, tv_series_productor, tv_series_director):
        if Person.ident > 9999999:
            raise Exception("Too many People")

        self.id = Person.ident
        Person.ident += 1
        self.name = name
        self.age = int(age)
        self.nationality = nationality
        self.biographie = biographie
        self.tv_series_actor = []
        self.tv_series_productor = []
        self.tv_series_director = []
        # on met 3 tableaux pour séparer les films dans lequel la star a officié en tant qu'acteur, producteur ou
        # réalisateur (souvent, les personnes auront 2 tableaux de vide, mais pour Woody Allen par exemple...)
