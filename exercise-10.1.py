'''EXERCISE 10.1: Revise a previous program as follows: Read and parse the “From” lines and pull out 
the addresses from the line. Count the number of messages from each person using a dictionary. After 
all the data has been read, print the person with the most commits by creating a list of (count, email) 
tuples from the dictionary. Then sort the list in reverse order and print out the person who has the 
most commits.'''

fhand = open('/home/alejandro/Documentos/Desarrollo/python/PY4E-ejercicios/mbox.txt', 'r')

dictionary = {}
final_list = []
max_list = []
max_final_list = []

for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    if words[1] in dictionary:
        dictionary[words[1]] += 1
    else:
        dictionary[words[1]] = 1

for key, val in list(dictionary.items()):
    final_list.append((val, key))
max_list.append(max(final_list))

for val, key in max_list:
    max_final_list.append((key, val))

print(max_final_list[0])