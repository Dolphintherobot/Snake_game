class snake:
    def __init__(self):
        """Purpose: create a snake class"""
        self.__body_position = []
        self.head = None
        self.tail = None

    def update_head_tail(self):
        '''Purpose: to update the head and tail of the snake,whenever it gets changed
        '''
        assert len(self.__body_position) != 0, "Cannot update an non-existant snake"
        self.head = self.__body_position[0]
        self.tail = self.__body_position[-1]
    
    def create_snake(self,grid):
        """Purpose:to create the snake whenever the game begins
        :param grid: a 2d list representing the board
        :note: will always place the head of the snake at the center of the board"""
        if len(self.__body_position) != 0:
            raise ValueError
        n = len(grid)
        m = len(grid[0])

        start_x = n//2
        start_y = m //2

        for i in range(1,5):
            self.__body_position.append((start_x,start_y))
            start_x -=1
            start_y -=1
    
        
