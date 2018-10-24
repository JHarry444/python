import re
with open("C:/Users/Jordan Harrison/Documents/BeeMovie.txt") as file:
    script = file.read()
    pattern = re.compile("(?<=\.\s)\w.*\.")
    matches = re.findall(pattern, script)
    print(matches)
    print(len(matches))
