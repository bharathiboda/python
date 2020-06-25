def is_perfect_number(num):
    total = 0
    for i in range(1, int(num/2+1)):
        if num % i == 0:
            total = total + i
    if total == num:
        print(num, " is a perfect num")
    else:
        print(num, " is not a perfect num")


def is_armstrong(num):
    original_num = num
    power_num = num
    total = 0
    power = 0
    while num != 0:
        power += 1
        num = num // 10
    while power_num != 0:
        digit = power_num % 10
        total = total + pow(digit, power)
        power_num = power_num // 10
    if total == original_num:
        print(original_num, " is a armstrong num")
    else:
        print(original_num, " is not a armstrong num")
