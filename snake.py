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


    def find_valid(self,grid):
        """Purpose:will find valid spaces for new tail so that it doesnt end the game
        :param grid: a 2d list representing the board
        :return: valid_spaces, a list of tuples, representing valid spaces
        """
        x,y = self.tail

        down = (x+1,y)
        left = (x,y-1)
        up = (x-1,y)
        right = (x,y+1)

        n = len(grid)
        m = len(grid[0])

        valid_spaces = [down,left,up,right]
        copy = valid_spaces.copy()
        for space in copy:
            x,y  = space
            if  0 > x > n -1 or 0 > y > m - 1 or space in self.__body_position:
                valid_spaces.remove(space)
        
        return valid_spaces


            

            
    
    def grow(self,grid):
        '''Purpose: to mimic enlarging the snake by adding to the list 
        :param grid: 2d list representing the board the snake is on
        :Post-conditions:will modify the body_position list by making it larger'''

        valid_spaces = self.find_valid(grid)
        space = valid_spaces[0]
        self.__body_position.append(space)
        self.update_head_tail()




    def game_over(self,grid):
        '''Purpose to check if the snake has ran out of bounds or into itself
        :param grid: a 2d list representing the board
        return True if the game is over,False otherwise'''

        n = len(grid)
        m = len(grid[0])
        x,y = self.head

        out_of_bounds = x < 0 or x > n-1 or y < 0 or y > m-1
        crash = self.head in self.__body_position[1:]

        return out_of_bounds or crash

    def place_snake(self,grid):
        '''Purpose: to map the coordinates of the snake onto the grid
        :param grid: a 2d list
        :Post-condition: will modify the contents of the list'''

        print(self.__body_position)
        for coord in self.__body_position:
            x,y = coord
            grid[x][y] = 1





        
    def compare_snakes(self,list,print_snake = False):
        """Purpose: test if body_position is storing the correct arguments
        :param list: a list of tuples you wish to compare
        :param print_snake: boolean indicating whether or not you want the body_position printed out
        return: True if the lists are the same,False otherwise"""

        if print_snake:
            print(self.__body_position)
        return self.__body_position == list

    
