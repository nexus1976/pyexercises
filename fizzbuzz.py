from typing import List

class FizzBuzz():
    def __init__(self) -> None:
        pass

    def run_transaction_script(self) -> bool:
        while True:
            print(f'\n')
            print('Please enter the maximum number for the FizzBuzz sequence (or x to exit):')
            response = input()
            if response:
                response = response.strip().lower()
                if response == 'x':
                    return False
                if response.isnumeric():
                    max = int(response)
                    print(f'Printing the first {max} items in a FizzBuzz sequence\n')
                    seq = self.fizzbuzz_sequence(max_items=max + 1)
                    for i in seq:
                        print(f'{i}\n')
                    print('Press enter to continue...')
                    input()
                    return True
    
    def fizzbuzz_sequence(self, max_items: int) -> List[str]:
        response = list()
        if max_items <= 1:
            return response
        for x in range(1, max_items):
            isFizz = x % 3 == 0
            isBuzz = x % 5 == 0
            isFizzBuzz = isFizz and isBuzz
            item = str(x)
            if isFizzBuzz:
                item = 'FizzBuzz'
            elif isFizz:
                item = 'Fizz'
            elif isBuzz:
                item = 'Buzz'
            response.append(item)
        return response