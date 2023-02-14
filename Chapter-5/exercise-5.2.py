# EXERCISE 5.2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

total = 0
count = 0
largest = None
smallest = None
while True:
    try:
        user_number = input('Enter a number: ')
        if user_number == 'done':
            break
        else:
            number = float(user_number)
            total = total + number
            count = count + 1
            if largest is None or number > largest:
                largest = number
            if smallest is None or number < smallest:
                smallest = number
    except:
        print('Invalid input')
#print(total)
#print(count)
print(largest)
print(smallest)
