# Mad Libs Generator Project

# Write code for the function random_noun, which takes in no inputs but outputs
# one of two nouns randomly. Use the randint function to generate a number
# from 0-1 and return a noun depending on whether the number is equal to 0 or 1.
# Feel free to experiment with different nouns, but for submission purposes return
# the string "sofa" if the number is 0, else return "llama".

from random import randint

def random_noun():
    # your code here
    number = randint(0, 1)
    if number == 0:
        return 'sofa'
    else:
        return 'llama'

print random_noun()
