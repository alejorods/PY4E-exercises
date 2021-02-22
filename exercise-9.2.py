# EXERCISE 9.2: Write a program that categorizes each mail message by
# which day of the week the commit was done. To do this look for lines
# that start with “From”, then look for the third word and keep a running
# count of each of the days of the week. At the end of the program print
# out the contents of your dictionary (order does not matter).

fhand = open('/home/alejandro/Documentos/Desarrollo/python/PY4E-ejercicios/mbox-short.txt', 'r')
dictionary = {}
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    if words[2] in dictionary:
        dictionary[words[2]] += 1
    else:
        dictionary[words[2]] = 1
print(dictionary)