# EXERCISE 6.3: 

def count(word,letter):
    counter = 0
    for value in word:
        if value == letter:
            counter = counter + 1
    print(counter)

count('banana','a')
