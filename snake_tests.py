import snake as s




def test_create_snake(dict):
    '''Purpose: to test the create_snake method
    :param dict: a dictionary containing the test cases,expected outputs and reasons for testing
    :return: None
    Post-conditions: will print error on console if expected !=actual output'''

    
    for test in dict:

        a_snake = s.Snake() 
        grid  = [[n for n in range(15)]for m in range(15)]
        a_snake.create_snake(grid)
        expected = dict[test][0]
        actual = a_snake.compare_snakes(expected)
        reason = dict[test][1]
        if not actual and a_snake.head != expected[0] and a_snake.tail != expected[-1]:
            print(f"error with input {test} actual was {actual}, expected was {expected},reason:{reason}")




create_snake_tests = {
    #test_number:(expected,reason)
    1:([(7,7),(6,7),(5,7),(4,7)],"Check if creates correctly"),
}


test_create_snake(create_snake_tests)



##################################################
#test movement 

#test move right 


grid  = [[n for n in range(15)]for m in range(15)]
a_snake = s.Snake()

test = "move_right and change_pos"

reason = "check move right method"
a_snake.create_snake(grid)
a_snake.move_right()

expected = [(7,8),(7,7),(6,7),(5,7)]


if not a_snake.compare_snakes(expected):
    print(f"error with {test} reason is {reason}")


#test move_left

test = "move_left and change_pos"

reason = "check move left method"

a_snake.move_left()
expected = [(7,7),(7,8),(7,7),(6,7)]
if not a_snake.compare_snakes(expected):
    print(f"error with {test} reason is {reason}")

#test move_up

test = "move_up and change_pos"

reason = "check move up method"

a_snake.move_up()
expected = [(6,7),(7,7),(7,8),(7,7)]


if not a_snake.compare_snakes(expected) or a_snake.head != expected[0] or a_snake.tail !=expected[-1]:
    print(f"error with {test} reason is {reason}")


#test move_down

test = "move_down and change_pos"

reason = "check move down method"

a_snake.move_down()
expected = [(7,7),(6,7),(7,7),(7,8)]
if not a_snake.compare_snakes(expected) or a_snake.head != expected[0] or a_snake.tail !=expected[-1]:
    print(f"error with {test} reason is {reason}")






#test grow



test = "grow and find_valid methods"

reason = "check grow method"

a_snake = s.Snake()
a_snake.create_snake(grid)

a_snake.grow(grid)
expected = [(7,7),(6,7),(5,7),(4,7),(4,6)]
if not a_snake.compare_snakes(expected) or a_snake.head != expected[0] or a_snake.tail !=expected[-1]:
    print(f"error with {test} reason is {reason}")




#test grow

a_snake = s.Snake()

a_snake.create_snake(grid)
#[(7,7),(6,7),(5,7),(4,7)]

n = 0

while n!= 11:
    n+=1
    a_snake.move_down()


test = "grow and find_valid methods"

reason = "check grow method when space is invalid"

a_snake.grow(grid)
expected = [(18,7),(17,7),(16,7),(15,7),(15,6)]
if not a_snake.compare_snakes(expected) or a_snake.head != expected[0] or a_snake.tail !=expected[-1]:
    print(f"error with {test} reason is {reason}")


#test grow


a_snake = s.Snake()

a_snake.create_snake(grid)
#[(7,7),(6,7),(5,7),(4,7)]

a_snake.move_down()
a_snake.move_up()
a_snake.move_down()


#known bug the snake can move across itself

test = "grow and find_valid methods"

reason = "check grow method when space is in the body_position list"

a_snake.grow(grid)
expected = [(8,7),(7,7),(8,7),(7,7),(7,6)]

if not a_snake.compare_snakes(expected) or a_snake.head != expected[0] or a_snake.tail !=expected[-1]:
    print(f"error with {test} reason is {reason}")





######################test game over


a_snake = s.Snake()

a_snake.create_snake(grid)
#[(7,7),(6,7),(5,7),(4,7)]

a_snake.move_down()
a_snake.move_up()
a_snake.move_down()
#[(8,7),(7,7),(8,7),(7,7)]


#known bug the snake can move across itself

test = "game over method"

reason = "check when head coordinates are in the body"

expected = True
actual = a_snake.game_over(grid)


if actual != expected:
    print(f"error with {test} reason is {reason}")






a_snake = s.Snake()

a_snake.create_snake(grid)
#[(7,7),(6,7),(5,7),(4,7)]


for n in range(15):
    a_snake.move_down()





test = "game over method"

reason = "check when y coordinate is out of bounds"

expected = True
actual = a_snake.game_over(grid)


if actual != expected:
    print(f"error with {test} reason is {reason}")









a_snake = s.Snake()

a_snake.create_snake(grid)
#[(7,7),(6,7),(5,7),(4,7)]


for n in range(15):
    a_snake.move_right()





test = "game over method"

reason = "check when x coordinate is out of bounds"

expected = True
actual = a_snake.game_over(grid)


if actual != expected:
    print(f"error with {test} reason is {reason}")






a_snake = s.Snake()

a_snake.create_snake(grid)
#[(7,7),(6,7),(5,7),(4,7)





test = "game over method"

reason = "check when game is not over"
expected = False
actual = a_snake.game_over(grid)


if actual != expected:
    print(f"error with {test} reason is {reason}")
