from Data_model import *

class Query_engine :


    def find_path(start_table : str , target_table : str ):

        queue : list(list(str , tuple(tuple))) = [[start_table ,()]]
        visited : set = {start_table}
        current_table : str = start_table

        while queue[0] !=  None :
            for step in Data_model.get_neighbours(current_table) :
                

            