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
if not a_snake.compare_snakes(expected) and a_snake.head != expected[0] and a_snake.tail !=expected[-1]:
    print(f"error with {test} reason is {reason}")


#test move_down

test = "move_down and change_pos"

reason = "check move down method"

a_snake.move_down()
expected = [(7,7),(6,7),(7,7),(7,8)]
if not a_snake.compare_snakes(expected,True) and a_snake.head != expected[0] and a_snake.tail !=expected[-1]:
    print(f"error with {test} reason is {reason}")