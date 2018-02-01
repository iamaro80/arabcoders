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

for i in list_of_words2:
    if i in parts_of_speech:
        x = raw_input('Enter '+i+' : ')
        replaced.append(x)
    else:
        replaced.append(i)


print replaced
print ' '.join(replaced)
