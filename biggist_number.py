# biggist_number
# it needs enhancement to determine if there are two biggest numbers

def bigger(a,b):
	if a > b:
		return a
	else:
		return b


def biggest(a,b,c):
	return bigger(bigger(a,b),c)

# the same behaivour using max 

def max_number(a, b, c):
	return max(a,b,c)


# Test Cases

print biggest(3, 6, 9)
#>>> 9

print biggest(6, 9, 3)
#>>> 9

print biggest(9, 3, 6)
#>>> 9

print biggest(3, 3, 9)
#>>> 9

print biggest(9, 3, 9)

# Test Cases : max_number
print max_number(15,2,3)