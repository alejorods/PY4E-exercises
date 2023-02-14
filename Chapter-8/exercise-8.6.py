'''EXERCISE 8.6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end 
when the user enters “done”. Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the 
maximum and minimum numbers after the loop completes.'''

user_list = []
while True:
    try:
        user_number = input('Enter a number: ')
        if user_number == 'done':
            break
        else:
            number = float(user_number)
            user_list.append(number)
    except:
        print('Invalid input')
print('The maximum number of the list is', max(user_list), 'while the minimum is', min(user_list), '.')
