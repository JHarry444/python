import re
string = "Peter Piper picked a peck of pickled peppers."
pattern = re.compile('[pP]\w*r')
match = re.findall(pattern, string)
print(match)
