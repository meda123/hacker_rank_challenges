# Challenge: Given a string of letters as input, output the letters in order of 
# how often they occur in the input string. In your output, each letter should 
# be on it's own line. 

# Note 1: If there's a tie, the order output should be alphabetical.   

from operator import itemgetter

"""
test1 = "a bb rrrr yyy"
Output: 
r
y
b
a

test2: "mm nn ooo pppp"
Output:
p
o
m
n
"""

def letter_frequency():
    all_letters = list(''.join(raw_input().split()))

    test = [(x,all_letters.count(x))for x in set(all_letters)]
    sort_test = sorted(test, key=lambda (k,val): val)
    sort_alpha = sorted(sort_test, key=itemgetter(1), reverse=True)

    for item in sort_alpha:
        print item[0] 

letter_frequency()   