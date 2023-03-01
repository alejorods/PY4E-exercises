'''Exercise 3: Write a program that reads a file and prints the letters
in decreasing order of frequency. Your program should convert all the
input to lower case and only count the letters a-z. Your program should
not count spaces, digits, punctuation, or anything other than the letters
a-z. Find text samples from several different languages and see how
letter frequency varies between languages.'''

import string

fhand = open('/home/alejandro/Documentos/Desarrollo/python/PY4E-ejercicios/romeo.txt', 'r')

dictionary = {}

for line in fhand:
    line = line.translate(str.maketrans('','',string.punctuation+'1234567890'))
    line = line.lower()
    words = line.split()
    for word in words:
        letters = tuple(word)
        for letter in letters:
            if letter in dictionary:
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1

lst = []
for key, value in list(dictionary.items()):
    lst.append((value,key))

lst.sort(reverse=True)

new_lst = []
for key, value in lst:
    new_lst.append((value,key))

for key, value in new_lst:
    print(key,value)