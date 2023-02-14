'''EXERCISE 9.3: Write a program to read through a mail log, build a histogram using a dictionary to count 
how many messages have come from each email address, and print the dictionary.'''

fhand = open('/home/alejandro/Documentos/Desarrollo/python/PY4E-ejercicios/mbox-short.txt', 'r')
dictionary = {}
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    if words[1] in dictionary:
        dictionary[words[1]] += 1
    else:
        dictionary[words[1]] = 1
print(dictionary)
