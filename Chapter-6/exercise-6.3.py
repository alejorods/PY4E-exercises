'''EXERCISE 6.3: Encapsulate this code 

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

in a function named count, and generalize it so that it accepts the string and the letter as arguments.'''

def count(word,letter):
    counter = 0
    for value in word:
        if value == letter:
            counter = counter + 1
    print(counter)

count('banana','a')
