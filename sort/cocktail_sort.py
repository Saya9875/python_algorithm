import random
import time


def cocktail_sort(numbers: list[int]) -> list[int]:
    """
    O(n**2)
    """
    len_numbers = len(numbers)
    swapped = True
    start = 0
    end = len_numbers - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end = end - 1

        for i in range(end-1, start-1, -1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True

        start = start + 1

    return numbers


random_int_list = random.sample(range(1, 11), 10)

start_time = time.time()
print(cocktail_sort(random_int_list))
end_time = time.time()
print("Processing time: ", end_time - start_time, "seconds")
