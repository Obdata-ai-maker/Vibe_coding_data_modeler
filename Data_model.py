import pandas
from Table import Column,Table

class Data_model :
    
    
    def __init__(self):
        # Instance variables
        self.tables : dict[str, Table] = {}

    
    def add_table(self,name : str, columns: dict[str, Column]):
            
            # validate dict and str instances
            if not isinstance(columns,dict):
                raise ValueError("error : columns are not passed as dictionary") 
            
            if not isinstance(name,dict):
                raise ValueError("error : table name  are not passed as string ")

            # normalize table name
            name = name.strip.lower()

            # check duplicate table → error
            if name in self.tables.keys : 
                 raise "error : table name duplicated"
            else : pass

            # normalize column names
            for i in columns :
               columns[i].name = columns[i].name.lower
            #    example (id , ("id" , "varchar10"))

            # detect duplicate columns → error
            # we have them stored in a dictionary no way there is duplicate keys
            # if we are talking about the values inside the columns dict then yes
            # create list
            lst = list()
            for i in columns :
                 lst.append(columns[i].name)

            for counter in lst : 
                 if lst.count(counter) >= 2 :
                    raise "error : table column duplicated"
                 else : pass
            
            # validate Column instances
            for i in columns :
                if not isinstance(columns[i],Column) :
                    raise "error : table columns  are not createad as Column Type " 
                else : pass
                 
            # create Table
            table = Table(name,columns)
            
            # store no need its in memory 




