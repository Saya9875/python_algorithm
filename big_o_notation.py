# O(log(n))
def func2(n):
    """
    func2(10)

    実行結果
    10
    5.0
    2.5
    1.25
    """
    if n <= 1:
        return
    else:
        print(n)
        func2(n/2)


# O(n)
def func3(numbers):
    """
    func3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    実行結果
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    """
    for num in numbers:
        print(num)


# O(n * log(n))
def func4(n):
    """
    func4(10)

    実行結果
    0 1 2 3 4 5 6 7 8 9
    0 1 2 3 4
    0 1
    0
    """
    for i in range(int(n)):
        print(i, end=' ')
    print()

    if n <= 1:
        return
    func4(n/2)


# O(n**2)
def func5(numbers):
    """
    func5([1, 2, 3, 4, 5])

    実行結果
    1 1
    1 2
    1 3
    1 4
    1 5

    2 1
    2 2
    2 3
    2 4
    2 5

    3 1
    3 2
    3 3
    3 4
    3 5

    4 1
    4 2
    4 3
    4 4
    4 5

    5 1
    5 2
    5 3
    5 4
    5 5
    """
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            print(numbers[i], numbers[j])
        print()


func5([1, 2, 3, 4, 5])
