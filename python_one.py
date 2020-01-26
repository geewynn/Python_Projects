# Write a Python function that accepts 
# a string and calculate the number of upper case letters and 
# lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def upper_and_lower(word):
    word_string = word
    upper_case = word_string.isupper()
    lower_case = word_string.islower()
    num_of_upper = print(len(upper_case))
    num_of_lower = print(len(lower_case))

    return num_of_upper, num_of_lower

upper_and_lower('God is GoodGG')
