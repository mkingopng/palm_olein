import re

pattern = re.compile("[0-9]")

if pattern.match("2 March"):
    print("True")
else:
    print("False")



