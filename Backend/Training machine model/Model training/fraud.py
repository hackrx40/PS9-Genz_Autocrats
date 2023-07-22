import re
from pdfminer.high_level import extract_pages, extract_text
text_1 = extract_text("Amazon 1a.pdf")
print(text_1)
pattern = re.compile(r"[a-zA-Z]+,{1}\s{1}")
matches = pattern.findall(text_1)
names_1 = [n[:-2] for n in matches]
print(names_1)

import re
from pdfminer.high_level import extract_pages, extract_text
text_2 = extract_text("Amazon 2a.pdf")
print(text_2)
pattern = re.compile(r"[a-zA-Z]+,{1}\s{1}")
matches = pattern.findall(text_2)
names_2 = [n[:-2] for n in matches]
print(names_2)

import re
from pdfminer.high_level import extract_pages, extract_text
text_3 = extract_text("Amazon 3a.pdf")
print(text_3)
pattern = re.compile(r"[a-zA-Z]+,{1}\s{1}")
matches = pattern.findall(text_3)
names_3 = [n[:-2] for n in matches]
print(names_3)