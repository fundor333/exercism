def square_of_sum(number):
    return sum(range(0, number + 1)) ** 2


def sum_of_squares(number):
    if number == 0:
        return 0
    else:
        return number * number + sum_of_squares(number - 1)


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
