import plotly.graph_objects as go
import kaleido
import pandas as pd
import seaborn
import pySankey
from pySankey import sankey

Sheet = 'Datensatz_01_2021.csv'
Data = []
f = open (Sheet, 'r', encoding='iso8859')
Datensatz = f.readlines()
for row in Datensatz:

    #row = row.replace(';"', '')
    #row = row.replace('"', '')
    rowdict =row.strip().split(';')
    if len(rowdict) == 8:
        for i in range(10):
            rowdict[1]=rowdict[1].replace(str(i), '')
            rowdict[5] = rowdict[5].replace(str(i), '')
        Data.append(rowdict)
    if len(rowdict) != 8:
        print(rowdict)
f.close()
#print(Data)
###########################




#########################
df = pd.DataFrame(Data)
df.columns = df.iloc[0]
df = df[1:]


print(df.head())

sankey.sankey(
    df['Abfahrtsland'], df['Ankunftsland'], aspect=10,
    fontsize=4, figure_name="sankeytest1"
)

if __name__ == '__main__':
    pass
    #print(Datensatz)


