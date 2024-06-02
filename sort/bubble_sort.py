import random
import time


def bubble_sort(numbers: list[int]) -> list[int]:
    """
    O(n**2)
    """
    numbers_count = len(numbers)
    for i in range(numbers_count):
        for j in range(numbers_count - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


ramdom_int_list = random.sample(range(1, 11), 10)

start_time = time.time()
print(bubble_sort(ramdom_int_list))
end_time = time.time()
print("Processing time: ", end_time - start_time, "seconds")
