import os
from fibonacci import Fibonacci
from averages import Averages
from fizzbuzz import FizzBuzz

def clearTerminal() -> None:
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def printMenu() -> None:
    clearTerminal()
    print(f'--------------------\n')
    print(f'1. Print Average of 2 Numbers\n')
    print(f'2. Print Fibonacci Sequence\n')
    print(f'3. Print FizzBuzz Sequence\n')
    print(f'\n')
    print('Press the x key to Exit')
    print(f'--------------------\n')

while True:
    printMenu()
    # print('Enter the number of the function that you wish to run (or x to exit):')
    response = input('Enter the number of the function that you wish to run (or x to exit): ')
    result = True
    if response:
        response = response.strip().lower()
        if response == 'x':
            break
        if response.isnumeric():
            selection = int(response)
            if selection == 1:
                prog = Averages()
                result = prog.run_transaction_script()
            if selection == 2:
                prog = Fibonacci()
                result = prog.run_transaction_script()
            if selection == 3:
                prog = FizzBuzz()
                result = prog.run_transaction_script()
            
            if result == False:
                break
