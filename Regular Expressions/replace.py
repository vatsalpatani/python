import re

str1 = "i am from gujarat"

res = re.sub(r"gujarat","rajkot",str1)

print(res)

# output  :   i am from rajkot