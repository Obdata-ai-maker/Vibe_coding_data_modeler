import pandas
from Table import Column,Table

class Data_model :
    
    DATA_TYPES = {"integer", "string", "date", "float", "bool"}
    
    def __init__(self):
        # Instance variables
        self.tables : dict[str, Table] = {}

    
    def add_table(self,tablename : str, columns : list[tuple[str,str]]):
            
            # validate dict and str instances
            if not isinstance(columns,list):
                raise ValueError("error : columns are not passed as list")
            if not columns : 
                raise ValueError(" columns list should be non null ")
            
            if not isinstance(tablename,str):
                raise ValueError("table name are not passed as string ")

            # normalize table name
            tablename = tablename.strip().lower()

            # check duplicate table → error
            # no need for keys()
            if tablename in self.tables : 
                 raise ValueError("error : table name duplicated")
            
            
            colvalide : dict[str, str] = {} # with type hint better initialise
            col: dict[str, Column] = {} # with type hint better initialise

            # validate Column instances
            # list are mutable 
            # !!!!!!!!!!!!! tuple are immutable !!!!!!!!!!

            for col_tuple in columns :
                if not isinstance(col_tuple, tuple) or len(col_tuple) != 2:
                    raise ValueError("Each column must be a tuple (name, type)")
                
                if not isinstance(col_tuple[0], str) or  not isinstance(col_tuple[1], str) :
                    raise ValueError("Each column and type must be a string non null ")
                
                col_name = col_tuple[0].strip().lower()
                col_type = col_tuple[1].strip().lower()

                if not col_name :
                     raise ValueError(f"error : column {col_name} should be non null  ")
                if not col_type :
                    raise ValueError(f"error : column type {col_type} should be non null ")

                if  col_name in colvalide :
                    raise ValueError(f"error : column {col_name} duplicated ")
                
                if col_type in self.DATA_TYPES  :
                        colvalide[col_name] = col_type
                        col[col_name] = Column(col_name,col_type )
                else  :
                        raise ValueError(f"error : column type {col_type} is invalid  ")
                        #colvalide[name] = "string"
                        # col[name] = Column(name,colvalide[name])


            table = Table(tablename,col)
            
            # we need store , its in memory inside the method not yet stored inside the instance

            self.tables[tablename] = table




