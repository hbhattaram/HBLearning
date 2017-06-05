# Testing strings and also all the methods associated with strings

name = "Harshit Bhattaram"
print(name)

test_string = "This is how we use a single 'quote' inside double quotes"
print(test_string)

test_string_1 = "Using newline \n and tab \t characters"
print(test_string_1)

# Using length function
value = len(name)
print(value)

# Using lower case
lower_case = name.lower()
print(lower_case)


# Using upper case
upper_case = name.upper()
print(upper_case)

# Using strip function
string_strip = name.strip()
print(string_strip)

# Using startswith Function
Value = name.startswith("Har")
print(Value)

# Using Endswith Function
Value1 = name.endswith("Har")
print(Value1)

# Using Replace function
Value2 = name.replace('Harshit', 'Revanth')
print(Value2)

# Using indexing
Value3 = name[1]
print(Value3)