import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

df = pd.read_excel('imiona.xlsx')
print(df)
#zad 1
# grupa = df.groupby(['Rok']).agg({'Liczba': ['sum']})
# wykres = grupa.plot(subplots=True, fontsize=20)
# plt.xlabel('Rok', fontsize=40)
# plt.ylabel('Ilosc urodzonych dzieci', fontsize=40)
# plt.show()
#zad 2
# grupa2 = df.groupby(['Plec']).agg({'Liczba': ['sum']})
# wykres2 = grupa2.plot.bar(subplots=True, fontsize=20)
# plt.legend(loc='lower right')
# plt.xlabel('Plec')
# plt.ylabel('Liczba dzieci w milionach')
# plt.show()
