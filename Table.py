import pandas
from Column import Column


class Table :
    def __init__(self, name : str, columns: dict[str, Column]):
        # Instance variables
        self.name = name.lower
        self.columns  = columns

        #    
        # example : 
        # (users , 
        # { 
        # (id , column("id" , "varchar10")),
        # (name , column("name" , "varchar25"))
        #}
        #),

