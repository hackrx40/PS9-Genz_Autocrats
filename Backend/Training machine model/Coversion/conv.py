import tabula
import pandas as pd

#LEGAL DOCUMENTS

D1 = tabula.convert_into("Amazon 1.pdf", "Amazon_1.csv", output_format="csv", pages='all')
D2 = tabula.convert_into("Amazon 2.pdf", "Amazon_2.csv", output_format="csv", pages='all')
D3 = tabula.convert_into("Amazon 3.pdf", "Amazon_3.csv", output_format="csv", pages='all')
D4 = tabula.convert_into("Amazon 4.pdf", "Amazon_4.csv", output_format="csv", pages='all')
D7 = tabula.convert_into("Amazon 7.pdf", "Amazon_7.csv", output_format="csv", pages='all')
D8 = tabula.convert_into("Amazon 8.pdf", "Amazon_8.csv", output_format="csv", pages='all')
D9 = tabula.convert_into("Amazon 9.pdf", "Amazon_9.csv", output_format="csv", pages='all')
 

invoice1 = pd.read_csv("Amazon_1.csv")
invoice2 = pd.read_csv("Amazon_2.csv")
invoice3 = pd.read_csv("Amazon_3.csv")
invoice4 = pd.read_csv("Amazon_4.csv")
invoice7 = pd.read_csv("Amazon_7.csv")
invoice8 = pd.read_csv("Amazon_8.csv")
invoice9 = pd.read_csv("Amazon_9.csv")



from pathlib import Path
invoice1.to_excel(Path.cwd() /"Same_Shape"/"invoice1.xlsx")
invoice2.to_excel(Path.cwd() /"Same_Shape"/"invoice2.xlsx")
invoice3.to_excel(Path.cwd() /"Same_Shape"/"invoice3.xlsx")
invoice4.to_excel(Path.cwd() /"Same_Shape"/"invoice4.xlsx")
invoice7.to_excel(Path.cwd() /"Same_Shape"/"invoice7.xlsx")
invoice8.to_excel(Path.cwd() /"Same_Shape"/"invoice8.xlsx")
invoice9.to_excel(Path.cwd() /"Same_Shape"/"invoice9.xlsx")

#Added:
import tabula
F2 = tabula.convert_into("FIR2.pdf", "FIR_2.csv", output_format="csv", pages='all')
F3 = tabula.convert_into("FIR3.pdf", "FIR_3.csv", output_format="csv", pages='all')
F5 = tabula.convert_into("FIR5.pdf", "FIR_5.csv", output_format="csv", pages='all')
F6 = tabula.convert_into("FIR6.pdf", "FIR_6.csv", output_format="csv", pages='all')
F7_1 = tabula.convert_into("FIR7.1.pdf", "FIR_7_1.csv", output_format="csv", pages='all')
F7_2 = tabula.convert_into("FIR7.2.pdf", "FIR_7_2.csv", output_format="csv", pages='all')
F7_3 = tabula.convert_into("FIR7.3.pdf", "FIR_7_3.csv", output_format="csv", pages='all')
F9 = tabula.convert_into("FIR9.pdf", "FIR_9.csv", output_format="csv", pages='all')




#FRAUD DOCUMENTS

DA1 = tabula.convert_into("Amazon 1a.pdf", "Amazon_1a.csv", output_format="csv", pages='all')
DA2 = tabula.convert_into("Amazon 2a.pdf", "Amazon_2a.csv", output_format="csv", pages='all')
DA3 = tabula.convert_into("Amazon 3a.pdf", "Amazon_3a.csv", output_format="csv", pages='all')
DA4 = tabula.convert_into("Amazon 4a.pdf", "Amazon_4a.csv", output_format="csv", pages='all')
DA7 = tabula.convert_into("Amazon 7a.pdf", "Amazon_7a.csv", output_format="csv", pages='all')
DA8 = tabula.convert_into("Amazon 8a.pdf", "Amazon_8a.csv", output_format="csv", pages='all')
DA9 = tabula.convert_into("Amazon 9a.pdf", "Amazon_9a.csv", output_format="csv", pages='all')



inv_out1 = pd.read_csv("Amazon_1a.csv")
inv_out2 = pd.read_csv("Amazon_2a.csv")
inv_out3 = pd.read_csv("Amazon_3a.csv")
inv_out4 = pd.read_csv("Amazon_4a.csv")
inv_out7 = pd.read_csv("Amazon_7a.csv")
inv_out8 = pd.read_csv("Amazon_8a.csv")
inv_out9 = pd.read_csv("Amazon_9a.csv")


from pathlib import Path
inv_out1.to_excel(Path.cwd() /"Same_Shape"/"inv_out1.xlsx")
inv_out2.to_excel(Path.cwd() /"Same_Shape"/"inv_out2.xlsx")
inv_out3.to_excel(Path.cwd() /"Same_Shape"/"inv_out3.xlsx")
inv_out4.to_excel(Path.cwd() /"Same_Shape"/"inv_out4.xlsx")
inv_out7.to_excel(Path.cwd() /"Same_Shape"/"inv_out7.xlsx")
inv_out8.to_excel(Path.cwd() /"Same_Shape"/"inv_out8.xlsx")
inv_out9.to_excel(Path.cwd() /"Same_Shape"/"inv_out9.xlsx")


