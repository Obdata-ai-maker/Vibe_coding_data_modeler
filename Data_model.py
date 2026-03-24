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
            
            if not isinstance(name,str):
                raise ValueError("error : table name  are not passed as string ")

            # normalize table name
            name = name.strip().lower()

            # check duplicate table → error
            # no need for keys()
            if name in self.tables : 
                 raise ValueError("error : table name duplicated")
            
            # validate Column instances
            for i in columns :
                if not isinstance(columns[i],Column) :
                    raise ValueError("error : table columns  are not createad as Column Type ") 
            

            # normalize column names
            for col in columns.values() :
               col.name = col.name.lower()
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
                    raise ValueError("error : table column duplicated")     
            # create Table
            table = Table(name,columns)
            
            # we need store , its in memory inside the method not yet stored inside the instance

            self.tables[name] = table




