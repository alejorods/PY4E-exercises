'''EXERCISE 3.2: Rewrite your pay program using try and except so that your program 
handles non-numeric input gracefully by printing a message and exiting the program.'''

try:
    hours = float(input('Enter hours: '))
    rate = float(input('Enter rate: '))
    if hours > 40:
        pay = (1.5 * (hours - 40) + 40) * rate
        print(pay)
    else:
        pay = hours * rate
        print(pay)
except:
    print('Error, please enter numeric input')
