'''EXERCISE 8.1: Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None. Then write 
a function called middle that takes a list and returns a new list that contains all but the first and last elements.'''

def chop(list):
    del list[0]
    del list[-1]

def middle(list):
    new_list = [list[0], list[-1]]
    return new_list 
