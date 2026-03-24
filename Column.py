import pandas

class Column :

    def __init__(self, name : str, type : str):
        # Instance variables
        self.name = name.lower()
        self.type = type