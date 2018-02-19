import string

data = '123ibrahim987'

test1 = string.maketrans('0123456789','9876543210')

test = data.translate(test1,'1')

print test


