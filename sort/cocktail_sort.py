import random
import time

def cocktail_sort(numbers: list[int]) -> list[int]:
    len_numbers = len(numbers)
    swapped = True
    start = 0
    end = len_numbers - 1
    while swapped:
        swapped = False
        for i in range(len_numbers - 1):
            if i % 2 == 0:
                if numbers[i] > numbers[i + 1]:
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                    swapped = True
        if not swapped:
            break
        swapped = False
        for i in range(len_numbers - 1, 0, -1):
            if i % 2 != 0:
                if numbers[i] < numbers[i - 1]:
                    numbers[i], numbers[i - 1] = numbers[i - 1], numbers[i]
                    swapped = True
    return numbers


random_int_list = random.sample(range(1, 11), 10)

start_time = time.time()
print(cocktail_sort(random_int_list))
end_time = time.time()
print("Processing time: ", end_time - start_time, "seconds")
