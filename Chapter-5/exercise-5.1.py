'''EXERCISE 5.1: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, 
and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message 
and skip to the next number.'''

total = 0
count = 0
while True:
    try:
        user_number = input('Enter a number: ')
        if user_number == 'done':
            break
        else:
            number = float(user_number)
            total = total + number
            count = count + 1
    except:
        print('Invalid input')
print(total)
print(count)
print(total/count)
