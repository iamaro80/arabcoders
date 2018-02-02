# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

def product_list(list_of_numbers):
    index  = 0
    total = 1
    while index < len(list_of_numbers):
        total = total * list_of_numbers[index]
        index += 1
    return total


#print product_list([9])
#>>> 9

#print product_list([1,2,3,4])
#>>> 24

#print product_list([])
#>>> 1
################################################################################

# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    index  = 0
    greatest = 0
    while index < len(list_of_numbers):
        if list_of_numbers[index] > greatest:
            greatest = list_of_numbers[index]
        index += 1
    return greatest




#print greatest([4,23,1])
#>>> 23
#print greatest([])
#>>> 0

################################################################################
# Let's play around with one more string method: string.split(), which
# splits a string into a list of substrings, and returns it as a new list.
# Assign list_of_words1 to the split string1 and list_of_words2 to the split string2.

string1 = "Yesterday, PERSON and I went to the PLACE. On our way, we saw a ADJECTIVE NOUN on a bike."
string2 = "PLACE is located on the ADVERB side of Dublin. near the mainly ADJECTIVE areas of PLACE."
list_of_words1 = string1.split()
list_of_words2 = string2.split()

#print list_of_words1
#print list_of_words2

parts_of_speech = ['VERB', 'PLACE', 'NAME', 'NOUN','PERSON','ADJECTIVE','ADVERB' ]
replaced = []


# for i in list_of_words2:
#     if i in parts_of_speech:
#         x = raw_input('Enter '+i+' : ')
#         replaced.append(x)
#     elif i[:-1] in parts_of_speech:
#         x = raw_input('Enter '+i+' : ')
#         replaced.append(x+'.')
#     else:
#         replaced.append(i)
#
#
# print replaced
# print ' '.join(replaced)
################################################################################
# Here's another chance to practice your for loop skills. Write code for the
# function word_in_pos (meaning word in parts_of_speech), which takes in a string
# word and a list parts_of_speech as inputs. If there is a word in parts_of_speech
# that is a substring of the variable word, then return that word in parts_of_speech,
# else return None.


# def word_in_pos(word, parts_of_speech):
#     for i in parts_of_speech:
#         if word.find(i) != -1:
#             return i
#
#
#
# test_cases = ["NOUN", "FALSE", "<<@PERSON><", "PLURALNOUN"]
# parts_of_speech = ["PERSON", "PLURALNOUN", "NOUN"]
#
# print word_in_pos(test_cases[0], parts_of_speech)
# print word_in_pos(test_cases[1], parts_of_speech)
# print word_in_pos(test_cases[2], parts_of_speech)
# print word_in_pos(test_cases[3], parts_of_speech)

################################################################################

# Write code for the function play_game, which takes in as inputs parts_of_speech
# (a list of acceptable replacement words) and ml_string (a string that
# can contain replacement words that are found in parts_of_speech). Your play_game
# function should return the joined list replaced, which will have the same structure
# as ml_string, only that replacement words are swapped out with "corgi", since this
# program cannot replace those words with user input.

parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

test_string = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

def play_game(ml_string, parts_of_speech):
    replaced = []
    ml_string = ml_string.split()
    for i in ml_string:
        rep = word_in_pos(i, parts_of_speech)
        if rep != None:
            user_input = raw_input('Type in a: '+rep)
            i = i.replace(rep,user_input)
            replaced.append(i)
        else:
            replaced.append(i)
    return ' '.join(replaced)

print play_game(test_string, parts_of_speech)
