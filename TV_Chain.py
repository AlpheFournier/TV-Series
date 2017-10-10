class TV_Chain:

    ident = 1000000

    def __init__(self, id, name, list_of_series):
        if TV_Chain.ident > 9999999:
            raise Exception ("Too many chains")

        self.id = TV_Chain.ident
        TV_Chain.ident += 1
        self.name = name
        self.list_of_series = []

