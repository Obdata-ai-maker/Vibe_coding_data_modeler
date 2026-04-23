from Data_model import *

class Query_engine :


    def find_path(start_table : str , target_table : str ):

        queue : list(list(str , list(tuple))) = [[start_table ,[]],]
        visited : set = {start_table}
        current_table : str = start_table
        path = []

        #iteration 2 : explore B : dequeue (B,[A -> B]) :  B has E and F neighbours    queue : ((C,[A -> C]),(D,[A -> D]),(E,[A -> B,B -> E]),(F,[A -> B,B -> F]))
        while queue[0] !=  None :
            current_table = queue[0][0]
            for step in Data_model.get_neighbours(current_table) :
                # current_table = step[0]
                path = [(current_table,step)]  if queue[0][0] == []  else [queue[0][0],queue (current_table,step)] 
                queue.append(step[1],path)
                visited.add(step[1])
                if step[1] == target_table : 
                    break 
            queue.pop(0)                

            