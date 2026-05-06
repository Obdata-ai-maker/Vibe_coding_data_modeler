import pandas
from Table import Column,Table
from Relationship import Relashionship

class Data_model :
    
    DATA_TYPES = {"integer", "string", "date", "float", "bool"}
    
    def __init__(self):
        # Instance variables
        self.tables : dict[str, Table] = {}
        self.Relashionships : list[Relashionship] = []

    
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

    def add_Relashionship(self, left_table : str, left_column : str ,
                 right_table : str, right_column : str) :
        
        # inputs are strings
        # normalized
        # tables exist
        # columns exist
        # types match
        # no exact duplicate (same tuple)
        # allow self-relationships
        # disallow reverse relationships

        if not left_table :
            raise ValueError(" left table should be non null ")
        
        if not left_column :
             raise ValueError(" left column should be non null ")
        
        if not right_table :
            raise ValueError(" right table should be non null ")
        
        if not right_column :
             raise ValueError(" right column should be non null ")
        
        # inputs are strings
        if not isinstance(left_table,str):
            raise ValueError("error : columns are not passed as str")
        
        if not isinstance(left_column,str):
            raise ValueError("error : columns are not passed as str")
        
        if not isinstance(right_table,str):
            raise ValueError("error : columns are not passed as str")
        
        if not isinstance(right_column,str):
            raise ValueError("error : columns are not passed as str")

        # normalized
        left_table = left_table.strip().lower()
        left_column = left_column.strip().lower()
        right_table = right_table.strip().lower()
        right_column = right_column.strip().lower()

        # tables exist
        if left_table not in self.tables or  right_table not in self.tables :
             raise ValueError("error : tables don't exist")
             
            # columns exist
        if left_column not in self.tables[left_table].columns or right_column not in self.tables[right_table].columns:
            raise ValueError("error : column tables don't exist")

                  
                # types match
        if self.tables[left_table].columns[left_column].type != self.tables[right_table].columns[right_column].type:
            raise ValueError("error : column types  don't match")
        
        if left_table == right_table and right_column == left_column :
            raise ValueError("error : self Relashionship with same column not allowed")
        
        for element in self.Relashionships :
            if element.right_table == left_table and element.left_table == right_table and element.right_column == left_column and element.left_column == right_column :
                raise ValueError("error : Relashionship duplicated")
            
            if element.left_table == left_table and element.right_table == right_table and element.left_column == left_column and element.right_column == right_column :
                raise ValueError("error : Relashionship duplicated")
            

            # later improvements
            # Define:

            # new_left  = (left_table, left_column)
            # new_right = (right_table, right_column)

            # For each existing:

            # existing_left  = (element.left_table, element.left_column)
            # existing_right = (element.right_table, element.right_column)

            # Then:

            # duplicate if:
            # (existing_left == new_left AND existing_right == new_right)
            # OR
            # (existing_left == new_right AND existing_right == new_left)
                
        self.Relashionships.append(Relashionship(left_table,left_column,right_table,right_column))       
   
    
def get_neighbours(self, target_table : str) : 
    lst : list[tuple] = [] 

    target_table = target_table.strip().lower() 
    if target_table not in self.tables : 
        raise ValueError("error : table not existent ") 
    
    for rel in self.Relashionships : 
        
        if target_table == rel.left_table : 
            lst.append((rel.left_table,rel.right_table,rel.left_column,rel.right_column)) 
        
        if target_table == rel.right_table : 
            lst.append((rel.right_table,rel.left_table,rel.right_column,rel.left_column)) 
            
    return lst