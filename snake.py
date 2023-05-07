class Snake:
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
    
        self.update_head_tail()



    

    def change_pos(self):
        '''Purpose:to modify the contents of the list such that it mimics a movement on the board
        :Post-conditions: will change the contents of self.__body_position'''

        self.__body_position.pop()
        self.__body_position.insert(0,self.head)
        self.update_head_tail()
    

    def move_up(self):
        '''Purpose: to move the snake upwards by 1 unit on the board
        :Post-conditions: will change the contents of self.__body_position'''

        x,y = self.head
        self.head = (x-1,y)
        self.change_pos()
    

    def move_down(self):
        '''Purpose: to move the snake downwards by 1 unit on the board
        :Post-conditions: will change the contents of self.__body_position'''

        x,y = self.head
        self.head = (x+1,y)
        self.change_pos()
    
    def move_right(self):
        '''Purpose: to move the snake right by 1 unit on the board
        :Post-conditions: will change the contents of self.__body_position'''

        x,y = self.head
        self.head = (x,y+1)
        self.change_pos()

    def move_left(self):
        '''Purpose: to move the snake left by 1 unit on the board
        :Post-conditions: will change the contents of self.__body_position'''

        x,y = self.head
        self.head = (x,y-1)
        self.change_pos()


        
    def compare_snakes(self,list,print_snake = False):
        """Purpose: test if body_position is storing the correct arguments
        :param list: a list of tuples you wish to compare
        :param print_snake: boolean indicating whether or not you want the body_position printed out
        return: True if the lists are the same,False otherwise"""

        if print_snake:
            print(self.__body_position)
        return self.__body_position == list

    
