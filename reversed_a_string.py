# #reversed a string using slice() 

str_value="hello world"

reversed_str = str_value[::-1]

print(reversed_str)

# reversed a string using for loop

str_value="hello world"
reversed_str=""
for char in str_value:
    reversed_str=char+reversed_str
print(reversed_str)

# by using reversed() of string

str_value="hello"
reversed_str="".join(reversed(str_value))

print(reversed_str)

# reverse of string in different ways

