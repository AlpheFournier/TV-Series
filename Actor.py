class Person:

    list_of_person = {}

    def __init__(self,name,age, nationality, biographie, tv_series_actor, tv_series_productor, tv_series_director):

        self.name = name
        self.age = int(age)
        self.nationality = nationality
        self.biographie = biographie
        self.tv_series_actor = tv_series_actor[0]
        self.tv_series_productor = tv_series_productor[0]
        self.tv_series_director = tv_series_director[0]
        