from typing import List

class Fibonacci():
    def __init__(self) -> None:
        pass

    def run_transaction_script(self) -> bool:
        while True:
            print(f'\n')
            print('Please enter the maximum number of items for the Fibonacci sequence (or x to exit):')
            response = input()
            if response:
                response = response.strip().lower()
                if response == 'x':
                    return False
                if response.isnumeric():
                    max = int(response)
                    print(f'Printing the first {max} items in a Fibonacci sequence\n')
                    seq = self.fibonacci_sequence(max_items=max)
                    for i in seq:
                        print(f'{str(i)}\n')
                    print('Press enter to continue...')
                    input()
                    return True
    
    def fibonacci_sequence(self, max_items: int) -> List[int]:
        response = list()
        prevNbr = 1
        prevPrevNbr = 1
        if max_items > 0:
            for i in range(max_items):
                if (i == 0 or i == 1):
                    response.append(1)
                else:
                    currentNbr = prevNbr + prevPrevNbr
                    response.append(currentNbr)
                    prevPrevNbr = prevNbr
                    prevNbr = currentNbr
        return response