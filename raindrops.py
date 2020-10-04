"""
Your task is to convert a number into a string that
contains raindrop sounds corresponding to certain
potential factors.

The rules of raindrops are that if a given number:
  - has 3 as a factor, add 'Pling' to the result.
  - has 5 as a factor, add 'Plang' to the result.
  - has 7 as a factor, add 'Plong' to the result.
  - does not have any of 3, 5, or 7 as a factor, 
    the result should be the digits of the number.
    
EXAMPLES:

3 converts to Pling
20 converts to Plang
28 converts to Plong
15 converts to PlingPlang
63 converts to PlingPlong
70 converts to PlangPlong
34 converts to "34"

"""

def convert(number):
    drops = {
        3: 'Pling',
        5: 'Plang',
        7: 'Plong',
    }

    result = ''

    for key, value in drops.items():
        if int(number) % key == 0:
            result += value

    return result if result else str(number)
