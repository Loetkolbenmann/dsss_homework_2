import random


def get_random_int(min, max):
    """Returns a random integer in the given range
    ----------
    min : int
        The minimum possible value 
    max : int
         The maximum possible value 
         
    Returns
    -------
    int
        The chosen random integer    
    """
    return random.randint(min, max)


def get_random_arithmetic_operator():
    """Returns one of the arithmetic operators except division
    ----------
    
    Returns
    -------
    string
        The chosen operator
    """
    return random.choice(['+', '-', '*'])


def generate_problem(number1, number2, operator):
    """Generates a math-problem from given arguments.
    ----------
    number1 : int
        The first number (minuend in case of substraction)
    number2 : int 
        The second number (subtrahend in case of substraction)
    operator : string
        The operator of the generated mathematical problem
    
    Returns
    -------
    string
        The chosen operator
    int
        The answer to the problem
    """
    problem = f"{number1} {operator} {number2}"     #generate question string    
    if operator == '+': answer = number1 + number2
    elif operator == '-': answer = number1 - number2
    else: answer = number1 * number2
    return problem, answer

def math_quiz():
    """Starts a math-quiz.
    Rounds to play are set in the beginning. Then a for-loop is used in which a problem is generated and the answer of
    the user is collected and evaluated. After the last round, the score is displayed.
    """
    score = 0
    rounds_to_play = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for round_number in range(rounds_to_play):
        #generate problem
        number1 = get_random_int(1, 10)
        number2 = get_random_int(1, 5)
        operator = get_random_arithmetic_operator()
        PROBLEM, ANSWER = generate_problem(number1, number2, operator)
        
        #question the user
        print(f"\nQuestion: {PROBLEM}")
        try:
            useranswer = int(input("Your answer: "))
        except ValueError:
            print("Answer must be an integer.")
        
        #evaluate answer
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{rounds_to_play}")

if __name__ == "__main__":
    math_quiz()
