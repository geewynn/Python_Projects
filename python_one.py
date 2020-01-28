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


# Write a Python function that takes a number as a parameter and 
# check the number is prime or not.
# Note : A prime number (or a prime) is a natural 
# number greater than 1 and that has no positive 
# divisors other than 1 and itself.


def isprime(x):
    if x > 1:
    # check for factors
        for i in range(2,x):
            if (x % i) == 0:
                print("is not a prime number")
                break
        else:
            print("is a prime number")
        
    # if input number is less than
    # or equal to 1, it is not prime
    else:
        print("is not a prime number")

isprime(17)
