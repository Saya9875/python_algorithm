import random
import time


def in_order(numbers: list[int]) -> bool:
    return all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))

    # for i in range(len(numbers) - 1):
    #     if numbers[i] > numbers[i + 1]:
    #         return False
    # return True


def bogo_sort(numbers):
    random.shuffle(numbers)
    while not in_order(numbers):
        random.shuffle(numbers)
    return numbers


ramdom_int_list = random.sample(range(1, 11), 10)

start_time = time.time()
print(bogo_sort(ramdom_int_list))
end_time = time.time()
print("Processing time: ", end_time - start_time, "seconds")
