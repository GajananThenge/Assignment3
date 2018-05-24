'''
2.​ Problem Statement
Problem Statement 1:
Write a function to compute 5/0 and use try/except to catch the exceptions.
NOTE:​ ​The​ ​solution​ ​shared​ ​through​ ​Github​ ​should​ ​contain​ ​the​ ​source​ ​code​ ​used​ ​
and ​the​ ​screenshot​ ​of​ ​the​ ​output.
'''

def division(numerator,denominator):
    try:
        return numerator/denominator
    except Exception as ZeroDivisionError:
        return ("Denominator can't be zero")
    except Exception as e:
        return (e)
print(division(5,0))
