import pandas as pd
from OSRM_test import *
import ast
import webbrowser

df = pd.read_csv('routes.csv')

#print(len(ast.literal_eval(df.iloc[2]['location'])['route']))
print(ast.literal_eval(df.iloc[0]['location']).keys())
get_map(ast.literal_eval(df.iloc[0]['location'])).save('map.html')
webbrowser.open('map.html', new=2)
