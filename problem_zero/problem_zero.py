from utils.decorators import timer
from itertools import count

@timer
def find_odd_squares(odd_nums):
    counter = count(start=1, step=2)
    odd_num_gen = (next(counter) for _ in range(odd_nums))
    odd_sum = 0
    
    for num in odd_num_gen:
        odd_sum += num * num

    return odd_sum

def main():
    print(find_odd_squares(347000))

if __name__ == "__main__":
    main()