'''
2.​ Problem Statement
Problem Statement 1:
Write a function to compute 5/0 and use try/except to catch the exceptions.
NOTE:​ ​The​ ​solution​ ​shared​ ​through​ ​Github​ ​should​ ​contain​ ​the​ ​source​ ​code​ ​used​ ​
and ​the​ ​screenshot​ ​of​ ​the​ ​output.
'''

def division(numerator,denominator):
    try:
        result = numerator/denominator
    except Exception as ZeroDivisionError:
        print("Denominator can't be zero")
    except Exception as e:
        print(e)
division(5,0)
