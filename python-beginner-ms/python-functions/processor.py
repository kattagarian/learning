def process_numbers(values):
    numbers = []
    for value in values:
        if value.isdigit() == False:
            continue
        numbers.append(value)
    else:
        print('wtf')
    print(numbers)
    return numbers
