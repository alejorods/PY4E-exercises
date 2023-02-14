'''EXERCISE 4.7: Rewrite the grade program from the previous chapter using a function called 
computegrade that takes a score as its parameter and returns a grade as a string.'''

def computegrade(score):
    try:
        if score < 0.6:
            return 'F'
        elif score < 0.7:
            return 'D'
        elif score < 0.8:
            return 'C'
        elif score < 0.9:
            return 'B'
        elif score <= 1.0:
            return 'A'
        else:
            return 'Bad score'
    except:
        return 'Bad score'

a = computegrade(0.95)
print(a)
b = computegrade('perfect')
print(b)
c = computegrade(10.0)
print(c)
d = computegrade(0.75)
print(d)
e = computegrade(0.5)
print(e)




