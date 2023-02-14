'''EXERCISE 9.5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from 
(i.e., the whole email address). At the end of the program, print out the contents of your dictionary.'''

fhand = open('/home/alejandro/Documentos/Desarrollo/python/PY4E-ejercicios/mbox-short.txt', 'r')
dictionary = {}
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    domains = words[1].split('@')
    if domains[1] in dictionary:
        dictionary[domains[1]] += 1
    else:
        dictionary[domains[1]] = 1
print(dictionary)
