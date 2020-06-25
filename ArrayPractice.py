def max_of_array(array):
    max = array[0]
    for i in range(0, len(array)):
        if max < array[i]:
            max = array[i]
    print(max, " is a biggest of array")


def second_max(array):
    max = array[0]
    secondMax = 0
    for i in range(1, len(array)):
        if max < array[i]:
            secondMax = max
            max = array[i]
        elif secondMax < array[i]:
            secondMax = array[i]
    print(secondMax, " is a second biggest")


def third_max(array):
    max = array[0]
    second_max = 0
    third_max = 0
    for i in range(1, len(array)):
        if max < array[i]:
            third_max = second_max
            second_max = max
            max = array[i]
        elif second_max < array[i]:
            third_max = second_max
            second_max = array[i]
        elif third_max < array[i]:
            third_max = array[i]
    print(third_max)


def sort_array(array):
    for j in range(0, len(array)):
        for i in range(1, len(array) - j):
            if array[i - 1] > array[i]:
                temp = array[i]
                array[i] = array[i - 1]
                array[i - 1] = temp
    for i in range(0, len(array)):
        print(array[i])


def sum_of_array(array):
    total = 0
    for i in range(0, len(array)):
        total = total + array[i]
    print(total)


def transpose_array(array):
    for i in range(0, len(array)):
        for j in range(0, len(array[i])):
            array[i][j] = array[j][i]
    print_array(array)


def print_array(array):
    print("[", end="")
    for k in range(0, len(array)):
        print("[", end=" "),
        for l in range(0, len(array[k])):
            print(array[k][l], end="")
            if l != len(array) - 1:
                print(", ", end="")
        if l != len(array[k]):
            print("],", end=" ")
    if k != len(array):
        print("]", end="")


def given_largest(array, position):
    for i in range(0, len(array)):
        for j in range(1, len(array) - i):
            if array[j - 1] > array[j]:
                temp = array[j]
                array[j] = array[j - 1]
                array[j - 1] = temp
    if position > len(array) - 1:
        print("given position is out of bound index")
    else:
        print("element in the given position ", position, ", ", array[position])


def reverse_num(num):
    original_num = num
    reverse_num = 0
    while num != 0:
        digit = num % 10
        reverse_num = (reverse_num * 10) + digit
        num = num // 10
    print(reverse_num)
