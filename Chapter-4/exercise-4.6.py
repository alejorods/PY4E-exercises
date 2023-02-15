'''EXERCISE 4.6: Rewrite your pay computation with time-and-a-half for overtime and 
create a function called computepay which takes two parameters (hours and rate).'''

def computepay(hours,rate):
    if hours > 40:
        pay = (1.5 * (hours - 40) + 40) * rate
    else:
        pay = hours * rate
    return pay

x = computepay(45,10)
print(x)
