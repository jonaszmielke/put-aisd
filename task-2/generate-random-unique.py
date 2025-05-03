import random
import ctypes
import os

class UniqueSortedList:

    def __init__(self):
        self.data = []

    #binary search to determine whether the number already is in the list or return an index of where to insert it
    def find(self, number: int):
        start = 0
        end = len(self.data) - 1

        while start <= end:
            mid = (start + end) // 2
            if self.data[mid] == number:
                return True
            elif number < self.data[mid]:
                end = mid - 1
            else:
                start = mid + 1

        #When the loop finishes, start is the correct index to insert the number
        return start

    def insert(self, number: int):
        index = self.find(number)
        if index is True:
            return False

        self.data = self.data[:index] + [number] + self.data[index:]
        return True


def write(numbers: list[int], name):

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, f'datasets/{name}.txt')

    with open(file_path, 'w') as file:
        for number in numbers:
            file.write(str(number) + '\n')


def parse_count(s):
    """Parse a string like '10m', '100k', or '500' into an integer count."""
    s = s.strip()
    if s[-1].lower() == 'k':
        return int(s[:-1]) * 1000
    elif s[-1].lower() == 'm':
        return int(s[:-1]) * 1000000
    else:
        return int(s)
    

if __name__ == '__main__':

    n_str = input('How many numbers: ')
    n_int = parse_count(n_str)
    max_number = input('Numbers will be in range from 0 to max\n(Leave empty for max number in an int)\nmax: ')
    if max_number == '':
        bits = ctypes.sizeof(ctypes.c_int) * 8
        max_number = 2**(bits - 1) - 1
    else:
        max_number = int(max_number)

    if n_int > max_number:
        print("Too many numbers, the list won't be unique")
    else:
        sorted_list = UniqueSortedList()
        output_list = []
        
        i = 0
        while i < n_int:

            number = random.randint(0, max_number)
            unique = sorted_list.insert(number)
            if unique is True:
                output_list.append(number)
                i += 1

        write(output_list, n_str)
