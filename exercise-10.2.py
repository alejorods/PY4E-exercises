'''EXERCISE 10.2: This program counts the distribution of the hour of the day for each of the messages. 
You can pull the hour from the “From” line by finding the time string and then splitting that string 
into parts using the colon character. Once you have accumulated the counts for each hour, print out the 
counts, one per line, sorted by hour.''' 

fhand = open('/home/alejandro/Documentos/Desarrollo/python/PY4E-ejercicios/mbox-short.txt', 'r')

dictionary = {}

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    hours = words[5].split(":")
    if hours[0] in dictionary:
        dictionary[hours[0]] += 1
    else:
        dictionary[hours[0]] = 1

hour_list = []

for key, val in list(dictionary.items()):
    hour_list.append((key, val))

hour_list.sort()
print(*hour_list, sep = '\n')