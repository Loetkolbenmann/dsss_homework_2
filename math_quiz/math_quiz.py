import random


def get_random_int(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)


def get_random_arithmetic_operator():
    return random.choice(['+', '-', '*'])


def function_C(n1, n2, o):
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 - n2
    elif o == '-': a = n1 + n2
    else: a = n1 * n2
    return p, a

def math_quiz():
    s = 0
    pi = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(pi):
        n1 = get_random_int(1, 10); n2 = get_random_int(1, 5.5); o = get_random_arithmetic_operator()

        PROBLEM, ANSWER = function_C(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{pi}")

if __name__ == "__main__":
    math_quiz()
