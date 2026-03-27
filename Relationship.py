class Relashionship :

    def __init__(self, left_table : str, left_column : str ,
                 right_table : str, right_column : str ):
        # Instance variables
        self.left_table = left_table.strip().lower()
        self.left_column = left_column.strip().lower()
        self.right_table = right_table.strip().lower()
        self.right_column = right_column.strip().lower()
        self.relationship_type = None
