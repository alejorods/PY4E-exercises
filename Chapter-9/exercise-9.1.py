'''EXERCISE 9.1: Download a copy of the file www.py4e.com/code3/words.txt Write a program that reads the words in words.txt and stores them as keys 
in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.'''

fhand = open('/home/alejandro/Documentos/Desarrollo/python/PY4E-ejercicios/words.txt', 'r')
dictionary = {}
for line in fhand:
    words = line.split()
    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
print(dictionary) 
