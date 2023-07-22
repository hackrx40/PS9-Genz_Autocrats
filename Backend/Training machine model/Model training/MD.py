GENIUNE INVOICE

import re
from pdfminer.high_level import extract_pages, extract_text
text1 = extract_text("Amazon 1.pdf")
print(text1)
pattern = re.compile(r"[a-zA-Z]+,{1}\s{1}")
matches = pattern.findall(text1)
names1 = [n[:-2] for n in matches]
print(names1)


import re
from pdfminer.high_level import extract_pages, extract_text
text2 = extract_text("Amazon 2.pdf")
print(text2)
pattern = re.compile(r"[a-zA-Z]+,{1}\s{1}")
matches = pattern.findall(text2)
names2 = [n[:-2] for n in matches]
print(names2)


import re
from pdfminer.high_level import extract_pages, extract_text
text3 = extract_text("Amazon 3.pdf")
print(text3)
pattern = re.compile(r"[a-zA-Z]+,{1}\s{1}")
matches = pattern.findall(text3)
names3 = [n[:-2] for n in matches]
print(names3)