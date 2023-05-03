import re

txt = "we are learning python"
x = re.search("\s",txt)

print("the first whitespace is at ",x.start())


# output  :   
#     the first whitespace is at  2