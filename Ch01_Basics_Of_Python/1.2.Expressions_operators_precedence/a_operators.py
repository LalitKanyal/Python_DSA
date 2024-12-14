'''
1. Logical Operators
not	    unary negation
and	    conditional and
or	    conditional or
'''
e = 1
f = 2
# and operator
#Returns True if both statements are true	
print( e < 3 and f < 3)

# or operator
#Returns True if one of the statements is true	
print( e < 3 or f < 0)

# not
# Reverse the result, returns False if the result is true
print (not(e < 2))

print(e and f)
# 2


'''
2. Equality Operators

is	same identity
is not	different identity
==	equivalent
!=	not equivalent

'''
a = 1
b = 1
print(a is b)
print(a == b)

c = 2 
d = 3
print ( c is not d)
print ( c != d)

'''
3. Comparison Operators

<	less than
<=	less than or equal to
>	greater than
>=	greater than or equal to
'''
print("     ")
print(c < b)
print(c <= d)
print(c > d)
print(c >= d)

'''
4. Arithmetic Operators

+	addition
−	subtraction
*	multiplication
/	true division
//	integer division or Floor division
%	the modulo operator
** exponentiation

'''
aa = 100
bb = 200

print(aa + bb)
print (bb - aa)
print(aa * 2 + bb * 3)
print(bb / aa)
# 2.0


print( bb // aa)
# 2
print( bb % aa)

'''
5. Bitwise Operators

~	bitwise complement (prefix unary operator)
&	bitwise and
|	bitwise or
^	bitwise exclusive-or
<<	shift bits left, filling in with zeros
>>	shift bits right, filling in with sign bit
'''

'''
6. Sequence Operators
Each of Python's built-in sequence types (str, tuple, and list) support the following operator syntaxes:

s[j]	element at index j
s[start:stop]	slice including indices [start,stop)
s[start:stop:step]	slice including indices start, start + step, start + 2 * step, . . ., up to but not equalling or stop
s + t	concatenation of sequences
k * s	shorthand for s + s + s + . . . (k times)
val in s	containment check
val not in s	non-containment check


-----
zero indexing of sequences
negative indices
slicing
del
'''

print('amp' in 'example')
print('lal' not in 'lalit')
print('lal' in 'Lalit')

list1 = ['1', '2', '3', '4']
print(list1[0])
# 1
print(list1[0:3])
# ['1', '2', '3']

print(2*list1)
# ['1', '2', '3', '4', '1', '2', '3', '4']
