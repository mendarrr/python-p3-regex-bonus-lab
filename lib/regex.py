import re

my_pattern = r"[A-Z][a-z]*'*[a-z]\s[a-z' ]*today'*[a-z, ]*[?\.]+"
my_regex = re.compile(my_pattern)

