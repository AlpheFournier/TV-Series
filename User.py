class User:

    ident = 1000000

    def __init__(self, id, name, password, mail):
        if User.ident > 9999999:
            raise Exception ("Too many Users")

        self.id = User.ident
        User.ident += 1
        self.name = name
        self.password = password
        self.mail = mail

    @property
    def login(self):
        return "{0},{1}".format(self.mail,self.password)

