import plotly.graph_objects as go
import plotly.express as px
import kaleido
import pandas as pd
import numpy as np

Sheet = 'Datensatz_01_2021.csv'
Data = []
f = open (Sheet, 'r', encoding='iso8859')
Datensatz = f.readlines()
for row in Datensatz:

    #row = row.replace(';"', '')
    #row = row.replace('"', '')
    rowdict =row.strip().split(';')
    if len(rowdict) == 8:
        Data.append(rowdict)
    if len(rowdict) != 8:
        print(rowdict)
f.close()
#print(Data)
'''
df = pd.DataFrame(Data)
df.columns = df.iloc[0]
df = df[1:]
'''

#print(df.head())
#################################
LaenderNR = 0
Laenderdict = {}

source = []
target = []
value = []

label = []

for n in Data[1:]:
    Abfahrtsland = n[1]
    Ankunftsland = n[5]
    ##Ordne Land Nummer zu:
    for i in range(10):
        Abfahrtsland=Abfahrtsland.replace(str(i), '')
        Ankunftsland = Ankunftsland.replace(str(i), '')
    if Abfahrtsland not in Laenderdict:
        Laenderdict[Abfahrtsland]=LaenderNR
        label.append(Abfahrtsland)
        LaenderNR+=1
    if Ankunftsland not in Laenderdict:
        Laenderdict[Ankunftsland]=LaenderNR
        label.append(Ankunftsland)
        LaenderNR+=1
        #print(n)
    #########################
    if len(source)==0:
        source.append(Laenderdict[Abfahrtsland])
        target.append(Laenderdict[Ankunftsland])
        value.append(1)
    routeIn = 0
    for i in range(len(source)):
        if Laenderdict[Abfahrtsland] == source[i] and Laenderdict[Ankunftsland] == target[i]:
            value[i]+=1
            routeIn = 1
            #print(Abfahrtsland, Ankunftsland)
    if routeIn == 0:
        source.append(Laenderdict[Abfahrtsland])
        target.append(Laenderdict[Ankunftsland])
        value.append(1)
    #print(len(source))

print(source, target, value)


print(len(source))

#################################
##Farben definieren##
def random_color():
    #list(np.random.choice(range(256), size=3))
    color = 'rgb('+str(np.random.choice(range(256)))+','+str(np.random.choice(range(256)))+','+str(np.random.choice(range(256)))+')'
    return color

'''
"color": [
    px.colors.qualitative.Plotly[i % len(px.colors.qualitative.Plotly)]
    for i in nodes
],'''
Farbdict = {}
for key in Laenderdict:
    Farbdict[Laenderdict[key]] = px.colors.qualitative.Plotly[Laenderdict[key] % len(px.colors.qualitative.Plotly)]
print(Farbdict)
#################################

##Plot starten##
maxtry = 150
fig = go.Figure(go.Sankey(
   # arrangement = "snap",
    #node = {
        #"label": label,
        #"x": [0.2, 0.1, 0.5, 0.7, 0.3, 0.5],
        #"y": [0.7, 0.5, 0.2, 0.4, 0.2, 0.3],
        #'pad':10},  # 10 Pixels
    node = {
        "label": label,
        "color": [Farbdict[Laenderdict[i]] for i in label],
        #"x": [0.2, 0.1, 0.5, 0.7, 0.3, 0.5],
        #"y": [0.7, 0.5, 0.2, 0.4, 0.2, 0.3],
        #'pad':10},  # 10 Pixels
    },
    link = {
        "source": source[0:maxtry],
        "target": target[0:maxtry],
        "value": value[0:maxtry],
        "color": [Farbdict[i] for i in source[0:maxtry]],
        #"color": [random_color() for i in value[0:maxtry]]
    }
)
)

#################################
#fig = go.Figure()
img_width = 1600
img_height = 900
scale_factor = 0.5
fig.add_layout_image(
    dict(
        #source="europakarte.webp",
        source="https://upload.wikimedia.org/wikipedia/commons/b/be/Europe%2C_administrative_divisions_-_de_-_colored.svg",
        xref="x",
        yref="y",
        x=-1,
        y=6,
        sizex=6,
        sizey=8,
        sizing="stretch",
        opacity=0.5,
        layer="below"
    )
)
fig.update_layout(template="plotly_white")
######################################
fig.show()
#fig.write_image("test1.pdf")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
    #print(Datensatz)


