import re

# Define a string with phone numbers
stri = '''Hello, my name is John Doe. I am 25 years old. I live in New York City. My phone number is 123-456-7890 and 987-548-2004'''

# Find all phone numbers in the string
number = re.findall('\d{3}-\d{3}-\d{4}', stri)
print(number)  # Output: ['123-456-7890', '987-548-2004']

# Define a string with a call mention
stri2 = "on a random day, I got a call from +91 9876543210"

# Search if the string starts with 'on'
number2 = re.search('^on', stri2)
print(number2)  # Output: <re.Match object; span=(0, 2), match='on'>
if number2:
    print("Yes")  # Output: Yes
else:
    print("No")

# Define a string about an animal
stri3 = "Dog is a pet animal"

# Match the pattern 'D\w\w' at the start of the string
mat = re.match('D\w\w', stri3)
print(mat)  # Output: <re.Match object; span=(0, 3), match='Dog'>
print(mat.group())  # Output: Dog

# Define a string about the weather
stri4 = "on monday there is a chance of rain"

# Split the string at whitespace, limiting to 2 splits
print(re.split('\s', stri4, 2))  # Output: ['on', 'monday', 'there is a chance of rain']

# Substitute 'o' with 'f' in the string
print(re.sub('o', 'f', stri4))  # Output: 'fn mfnday there is a chance of rain'

# Find all occurrences of characters between 's' and 'v'
print(re.findall('[s-v]', stri4))  # Output: ['s', 't', 't', 'r', 's']

# Check if the string ends with 'rain'
print(re.findall("rain$", stri4))  # Output: ['rain']

# Define a string mentioning the day
stri5 = "Today is monday"

# Find if the string starts with 'Today' and ends with 'monday'
print(re.findall("^Today.*monday$", stri5))  # Output: ['Today is monday']

# Define a string mentioning locations
stri6 = "Delhi is in india and inside Asia"

# Find occurrences of 'in'
print(re.findall('in', stri6))  # Output: ['in', 'in', 'in', 'in']

# Find occurrences of 'in' followed by zero or more 'n's
print(re.findall('in*', stri6))  # Output: ['in', 'i', 'in', 'in', 'i', 'in', 'i']

# Find occurrences of 'in' followed by one or more 'n's
print(re.findall('in+', stri6))  # Output: ['in', 'in', 'in']

# Define a string with various words
stri7 = "Toy Today Tolayed PT MOnitor"

# Find words that start with 'T' and end with 'y'
for i in stri7.split():
    if re.findall('^T.*y$', i):
        print(i)  # Output: Toy, Today
