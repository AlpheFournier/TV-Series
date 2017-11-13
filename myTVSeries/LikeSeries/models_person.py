class Person():

    def __init__(self, dico):
        for i,j in dico.items():
            setattr(self,i,j)

    @property
    def name(self):
        return self.name

    @property
    def gender(self):
        return self.gender

    @property
    def birthday(self):
        return self.birthday

    @property
    def deathday(self):
        return self.deathday

    @property
    def biography(self):
        return self.biography

    @property
    def mark(self):
        return self.mark

    @name.setter
    def name(self, value):
        self._name = value

    @gender.setter
    def gender(self, value):
        self._gender = value

    @birthday.setter
    def birthday(self, value):
        self._birthday = value

    @deathday.setter
    def deathday(self, value):
        self._deathday = value

    @biography.setter
    def biography(self, value):
        self._biography = value

    @mark.setter
    def mark(self, value):
        self._mark = value