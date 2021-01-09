# EXERCISE 7.3:  Sometimes when 
# programmers get bored or want to 
# have a bit of fun, they add a 
# harmless Easter Egg to their 
# program. Modify the program that 
# prompts the user for the file 
# name so that it prints a funny 
# message when the user types in 
# the exact file name “na na boo 
# boo”. The program should behave 
# normally for all other files 
# which exist and don’t exist.

fname = input('Enter the file name: ')

try:
    fhand = open(fname, 'r')
except:
    if fname == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have benn punk'd!")
        exit()
    else:
        print('File cannot be opened: ', fname)
        exit()

count = 0
spam = 0

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        data = line
        zero_position = data.find('0')
        string = data[zero_position:]
        number = float(string)
        count = count + 1
        spam = spam + number

average_spam = spam / count
print('Average spam confidence: ', average_spam)