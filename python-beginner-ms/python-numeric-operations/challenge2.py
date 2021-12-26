print('Simple calculator!')

first_number = input('First number? ')

if first_number.isnumeric() == False:
    print('Please input a number')
    exit()

operation = input('Operation? ')

if operation != '+' and operation != '-' and operation != '*' and operation != '/' and operation != '%' and operation != '**':
    print('Operation not recognized')
    exit()

second_number = input('Second number? ')

if second_number.isnumeric() == False:
    print('Please input a number')
    exit()

if operation == '+':
    result = int(first_number) + int(second_number)
    print('Sum of {} + {} equals {}'.format(first_number, second_number, result))
elif operation == '-':
    result = int(first_number) - int(second_number)
    print('Difference of {} - {} equals {}'.format(first_number, second_number, result))
elif operation == '*':
    result = int(first_number) * int(second_number)
    print('Product of {} * {} equals {}'.format(first_number, second_number, result))
elif operation == '/':
    result = int(first_number) / int(second_number)
    print('Quotient of {} / {} equals {}'.format(first_number, second_number, result))
elif operation == '%':
    result = int(first_number) % int(second_number)
    print('Modulus of {} % {} equals {}'.format(first_number, second_number, result))
else:
    result = int(first_number) ** int(second_number)
    print('Exponent of {} ** {} equals {}'.format(first_number, second_number, result))