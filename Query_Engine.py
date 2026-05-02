from ntpath import join
from streamlit import empty
from Data_model import *

class Query_engine :


    def find_path(start_table : str , target_table : str ):

        queue : list(list(str,list(Relashionship)) )= [[start_table ,[]]]
        visited : set = {start_table}
        current_table : str = start_table
        path = []

        #iteration 2 : explore B : dequeue (B,[A -> B]) :  B has E and F neighbours    
        # queue : ((C,[A -> C]),(D,[A -> D]),(E,[(A -> B),(B -> E)]),(F,[A -> B,B -> F]))
        while queue :
            current_table = queue[0][0]
            for step in Data_model.get_neighbours(current_table) :
                relashionshipTable = step.right_table if step.left_table == current_table else step.left_table
                if relashionshipTable not in visited : 
                    # path = [(current_table,step[1])] if not queue[0][1] else queue[0][1]+ [(current_table,step[1])]
                    #i don't need the if because whats it was treating is path is null 
                    # so [] + [(current_table,step[1])] is the same as [(current_table,step[1])]
                    path = queue[0][1] + [step]
                    queue.append([relashionshipTable,path])
                    visited.add(relashionshipTable)
                    if relashionshipTable == target_table :
                            return path
            queue.pop(0)
        return None
    
    def sql_generator(start_table : str,path : list[Relashionship]) :
         
         query = f"""SELECT * FROM {start_table}"""
         query_tables = {start_table}
         for path1 in path :
                    if path1.left_table not in query_tables and path1.right_table in query_tables :
                        new_table = path1.right_table
                        left = path1.left_table
                        right = path1.right_table
                    elif path1.right_table in query_tables and path1.left_table not in query_tables:
                        new_table = path1.left_table
                        # need to rethink 
                        left = path1.left_table
                        right = path1.right_table
                    else:
                        continue

                    query += f""" join {new_table} on {left}.{path1.left_column} = {right}.{path1.right_column}"""
                    query_tables.add(new_table)

