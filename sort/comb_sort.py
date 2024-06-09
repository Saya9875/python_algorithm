import random
import time


def comb_sort(numbers: list[int]) -> list[int]:
    """
    Avarage O(n**2/2**p) where p is the number of increments
    """
    numbers_count = len(numbers)
    gap = numbers_count
    swapped = True
    while gap != 1 or swapped:
        gap = int(gap / 1.3)
        if gap < 1:
            gap = 1

        swapped = False

        for i in range(0, numbers_count - gap):
            if numbers[i] > numbers[i + gap]:
                numbers[i], numbers[i + gap] = numbers[i + gap], numbers[i]
                swapped = True

    return numbers


ramdom_int_list = random.sample(range(1, 11), 10)

start_time = time.time()
print(comb_sort(ramdom_int_list))
end_time = time.time()
print("Processing time: ", end_time - start_time, "seconds")
