# A regular expression or RegEx is a special text string that helps to find patterns in data.
# A RegEx can be used to check if some pattern exists in a differennt data type.
# To use RegEx in pythn first we should import the RegEx module which is called re.

import re

# re.match(): searches only in the beginning of the list of the string and returns matched objects if found, else returns None. 
# re.search(): Returns a match object if there is one anywhere in the string, including multiline strings.
# re.findall(): Returns a list containing all matches
# re.split(): Takes a string, splits it at the match points, returns a list
# re.sub(): Replaces one or many matches within a string

# MATCH

txt = "I love to learn Python and JavaScript"

match = re.match("I love to learn", txt, re.I)
# re.I means case ignore
print(match)
print(match.span())

start, end = match.span()
substring = txt[start: end]

print(substring)

txt =  "I love to leearn python and javascript"
match = re.match("I like to learn", txt, re.I)

print(match)

# SEARCH

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend pyhton for a first programming language'''

match = re.search("first", txt, re.I)
print(match.span())

start, end = match.span()
substring = txt[start:end]
print(substring)

# FINDALL

text = '''Python is the most beautiful language that a human being has ever created
I recommend python for a first programming language'''

matches = re.findall("language", text)
print(matches)
matches = re.findall("python", text)
print(matches)
matches = re.findall("python", text, re.I)
print(matches)
matches = re.findall("Python|python", text)
print(matches)
matches = re.findall("[Pp]ython", text)
print(matches)

# SUB

text = '''Python is the most beautiful language that a human being has ever created
I recommend python for a first programming language'''

match_replaced = re.sub("python", "JavaScript", text, flags=re.I)
print(match_replaced)
match_replaced = re.sub("Python|python", "JavaScript", text)
print(match_replaced)
match_replaced = re.sub("[Pp]ython","JavaScript", text)
print(match_replaced)

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub("%", "", txt)
print(matches)

# SPLIT

text = '''Python is the most beautiful language that a human being has ever created
I recommend python for a first programming language'''

print(re.split("\n", text))

# Writing RegEx Patterns

regex_pattern = r"apple"
text = "Apple and banana are fruits. An old cliche says an apple a day a doctor away.... a banana a day keeps the doctor far far away."

matches = re.findall(regex_pattern, text)
print(matches)
matches = re.findall(regex_pattern, text, re.I)
print(matches)

regex_pattern = r"[Aa]pple"
matchees = re.findall(regex_pattern, text)
print(matches)

regex_pattern = r"[Aa]pple|[Bb]anana"
matches = re.findall(regex_pattern, text)
print(matches)

regex_pattern = r"\d"
txt = "This regular expression example was made on December 1, 1999 and revised on February 11, 2026"
matches = re.findall(regex_pattern, txt)
print(matches)

# On eor more times(+)
regex_pattern = r"\d+"
print(re.findall(regex_pattern, txt))

regex_pattern = r"[a]." 
txt = '''Apple and banana are fruits'''
print(re.findall(regex_pattern, txt))

regex_pattern = r"[a].+"
print(re.findall(regex_pattern, txt))

txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r"[Ee]-?mail"
print(re.findall(regex_pattern, txt))

txt = "This regular expression example was made on December 1, 1999 and revised on February 11, 2026"
regex_pattern = r"\d{4}"
print(re.findall(regex_pattern, txt))
regex_pattern = r"\d{1,4}"
print(re.findall(regex_pattern, txt))

txt = "This regular expression example was made on December 1, 1999 and revised on February 11, 2026"
regex_pattern = r'^This'  # ^ means starts with
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']

text = "This regular expression example was made on December 1, 1999 and revised on February 11, 2026"
regex_pattern = r"[^A-Za-z ]+"
print(re.findall(regex_pattern, text))
