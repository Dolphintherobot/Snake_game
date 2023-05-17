
import pygame
import snake as s
import random as rn




def generate_apple(grid,apple_list):
    """Purpose: to generate an x,y coordinate to mark as an apple for the snake to pick up
    :param grid: 2d list representing the game board
    :param apple_list: a list of x,y coordinates representing apples
    :Post-conditions: will modify grid space to be 3 and update apple_list """

    n = len(grid)
    m = len(grid[0])

    x = rn.randint(0,n-1)
    y = rn.randint(0,m-1)

    if grid[x][y] == 1:
        generate_apple(grid,apple_list)
    else:
        grid[x][y] = 3
        apple_list.append((x,y))



def on_apple(head,apple_list):
    """Purpose: check if the snake is on an apple
    :param head: x,y coordinate, representing head of snake
    :param: apple_list: list of x,y coordinates
    :return True if head is on apple,False otherwise
    """
    return head in apple_list

def cover_tail(tail,grid):
    """Purpose: set the x,y of the tail back to 2 before the snake moves, to prevent infinite growth on the board
    :param tail: x,y coordinate, representing tail of snake
    :param: grid: 2d list
    :Post-conditions:will modify the board
    """
    x,y = tail
    grid[x][y] = 0



def default_move(direction,snake):
    '''Purpose:to move the snake in a direction if the player has not selected a key
    :param direction: string that can be 4 words: up,down,left or right
    :param snake: a snake object'''

    if direction == "right":
        snake.move_right()
    elif direction == "left":
        snake.move_left()
    elif direction == "up":
        snake.move_up()
    else:
        snake.move_down()



def draw_squares(screen,grid,height,width,margin):
    ''''Purpose: to draw the squares into the gui
    :parm screen: the display being drawn onto
    :param grid: a nested list,representing the array backed grid
    :param height:how tall you want the squares to be
    :param width: width of the squares
    :param margin: how much space between the squares
    '''

    n = len(grid) 
    m = len(grid[0]) 

    
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (255,255,0)

    for row in range(n):
        for column in range(m):
            color = WHITE
            if grid[row][column] == 3:
                color = RED
            elif grid[row][column] == 0:
                color = GREEN
            elif grid[row][column] == 1:
                color = YELLOW



            pygame.draw.rect(screen,
                             color,
                             [(margin + width) * column + margin,
                              (margin + height) * row + margin,
                              width,
                              height])       



def main(grid):
    '''
    Purpose:program that runs the gui
    :param grid: a 2d list'''
    pygame.init()
    size = (500, 500)
    screen = pygame.display.set_mode(size)
    
    
    a_snake = s.Snake()
    a_snake.create_snake(grid)
    list_of_apples = []

    height = 28
    width = 28    
    margin = 5
    
    done = False
    clock = pygame.time.Clock()

    direction = "right"
    n = 0

    has_moved = False
    while not done:
        for event in pygame.event.get():
            pygame.time.set_timer(event,5000)
            cover_tail(a_snake.tail,grid)
            if event.type == pygame.QUIT:
                done = True
                has_moved = True
            elif event.type == pygame.K_LEFT:
                a_snake.move_left()
                direction = "left"
                has_moved = True
            elif event.type == pygame.K_RIGHT:
                a_snake.move_right()
                direction = "right"
                has_moved = True
            elif event.type == pygame.K_DOWN:
                a_snake.move_down()
                direction = "down"
                has_moved = True
            elif event.type == pygame.K_UP:
                a_snake.move_up()
                direction = "up"
                has_moved = True
        

        if not has_moved:
            default_move(direction,a_snake)

        if on_apple(a_snake.head,list_of_apples):
            list_of_apples.remove(a_snake.head)
            a_snake.grow()
        
        if n ==3:
            generate_apple(grid)
            n = 0
        
        if a_snake.game_over(grid):
            done = True
            print("Out of bounds")
            continue



        a_snake.place_snake(grid)
        BLACK = (0,0,0)
        BLUE = (0,0,255)
        screen.fill(BLACK)
        draw_squares(screen,grid,height,width,margin)
        pygame.display.flip()
    
        clock.tick(60)
        n +=1
 

    pygame.quit()


n = 15 #how many rows 
m = 15 #how many columns
grid  = [[0 for x in range(n)] for y in range(m)]

main(grid)