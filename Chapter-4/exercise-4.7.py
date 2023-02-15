'''EXERCISE 4.7: Rewrite the grade program from the previous chapter using a function called 
computegrade that takes a score as its parameter and returns a grade as a string.'''

def computegrade(score):
    try:
        if score >= 0 and score < 0.6:
            print('F')
        elif score >= 0.6 and score < 0.7:
            print('D')
        elif score >= 0.7 and score < 0.8:
            print('C')
        elif score >= 0.8 and score < 0.9:
            print('B')
        elif score >= 0.9 and score <= 1.0:
            print('A')
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
