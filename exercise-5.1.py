# EXERCISE 5.1: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

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


# Incorrect way
'''
while True:
    try:
        total = 0
        count = 0
        user_number = input('Enter a number:')
        number = float(user_number)
        if user_number == 'done':
            break
        else:
            count = count + 1
            total = total + number
    except:
        print('Invalid input')
print(total)
print(count)
print(total/count)
'''
# Here I have two mistakes. The first one is that the accumulator and the counter should be out of the loop. The second mistake is the position of the number variable. The program reads the input and try to convert it to a float type. Then, when we write 'done' there is an Error and the except acts.
