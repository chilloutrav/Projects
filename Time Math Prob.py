import random
import time
OPERATORS = ["+", "-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generat_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    result = eval(expr)
    return expr, result
wrong = 0
start_time = time.time()
for i in range(TOTAL_PROBLEMS):
    expr, result = generat_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + "= ")
        if guess == str(result):
            break
        wrong += 1
end_time = time.time()
total_time = end_time - start_time

print("time took is", total_time)