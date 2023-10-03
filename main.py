def display_odd_numbers(start, end):
    if start % 2 == 0:
        start += 1

    for number in range(start, end + 1, 2):
        print(number)


display_odd_numbers(1, 10)

