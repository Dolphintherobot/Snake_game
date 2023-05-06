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
        actual = a_snake.compare_snakes(expected,True)
        reason = dict[test][1]
        if not actual and a_snake.head != expected[0] and a_snake.tail != expected[-1]:
            print(f"error with input {test} actual was {actual}, expected was {expected},reason:{reason}")




create_snake_tests = {
    #test_number:(expected,reason)
    1:([(7,7),(6,7),(5,7),(4,7)],"Check if creates correctly"),
}


test_create_snake(create_snake_tests)
