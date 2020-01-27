# Write a Python function that accepts 
# a string and calculate the number of upper case letters and 
# lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def upper_and_lower(word):
    upper = []
    lower = []
    for letter in word:
        if letter.isupper():
            upper.append(letter)
        elif letter.islower():
            lower.append(letter)
        else:
            pass

    num_of_upper = print(len(upper))
    num_of_lower = print(len(lower))


    return num_of_upper, num_of_lower

upper_and_lower('God is Good')
