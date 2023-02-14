'''EXERCISE 9.4: Add code to the above program to figure out who has the most messages in the file. After all the data has been read and the 
dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the 
most messages and print how many messages the person has.'''

fhand = open('/home/alejandro/Documentos/Desarrollo/python/PY4E-ejercicios/mbox.txt', 'r')
dictionary = {}
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    if words[1] in dictionary:
        dictionary[words[1]] += 1
    else:
        dictionary[words[1]] = 1
maximum = max(dictionary, key=dictionary.get)
# The second parameter 'key=dictionary.get' let the function to return the values of the dictionary. 
# Based on the values (rather than the dictionary's keys), the key having the maximum value is returned.
print(maximum, dictionary[maximum])
