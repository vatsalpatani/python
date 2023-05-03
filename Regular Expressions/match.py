import re

pattern = r"^abc"
mystr = "abcdef"

x = re.match(pattern,mystr)
print(x)

# output  :
#     <re.Match object; span=(0, 3), match='abc'>