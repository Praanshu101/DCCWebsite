import fitz
import csv
print(fitz.__doc__)
doc=fitz.open("DCC_Assinment_Website/IndComp.pdf")
w=csv.writer(open("IndComp.csv",'w',newline=''))
for page in doc:
    tab=page.find_tables()
    if tab.tables:
        w.writerows(tab[0].extract())