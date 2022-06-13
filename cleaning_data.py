import pandas as pd
import numpy as np

df = pd.read_csv('Refromate_data.csv', on_bad_lines='skip',encoding='latin-1', sep=',', usecols=["Abfahrtsdatum",
                        'Abfahrtsland', 'Sources', 'Ankunftsdatum', 'Ankunftsland', 'Destination'])
source_country = df['Abfahrtsland'].tolist()
des_country = df['Ankunftsland'].tolist()
Source_date = df['Abfahrtsdatum'].tolist()
Ending_date = df['Ankunftsdatum'].tolist()

source_coordinates = df['Sources'].str.replace('nan, nan', '').tolist()
destination_coordinates = df['Destination'].str.replace('nan, nan', '').tolist()
G_Start_date = []
G_End_date = []
G_Start_coordinates = []
G_End_coordinates = []

for val in range(len(source_country)):
    if source_country[val] == 'DE' and des_country[val] == 'DE':
        new= source_coordinates[val].replace("(", '')
        Anew = new.replace(')', '')
        G_Start_date.append(Source_date[val])
        G_Start_coordinates.append(Anew)
        new1= destination_coordinates[val].replace("(", '')
        Anew1 = new1.replace(')', '')
        G_End_date.append(Ending_date[val])
        G_End_coordinates.append(Anew1)

# for val in range(len(G_Start_coordinates)):
#     G_Start_coordinates[val].replace('(', '')
#     G_Start_coordinates[val].replace(')', '')

Header = {'Sdate': G_Start_date, 'SCoordinates': G_Start_coordinates, 'Edate': G_End_date,
          'ECoordinates': G_End_coordinates}
df1 = pd.read_csv('German_data.csv', sep=',')
'''
df2 = pd.DataFrame()
for i in range(df1.shape[0]):
    #print(df1.iloc[i])
    print(len(df1.iloc[i]))
    if len(df1.iloc[i]) == 4:

        df2 = df2.append(df1.iloc[i], ignore_index=True)
        df2.to_csv('Pure_data.csv', index=False, sep=',', header=True, encoding='utf-8', date_format=int)

#df1.to_csv('German_data.csv', index= False, sep=',', header= True, encoding= 'utf-8', date_format= int)'''

df2 = df1.dropna()

df3 = df1[df1.isna().any(axis=1)]
df3.to_csv('GermanDataWithoutEntries.csv',index=False)

df2['s_lat'] = df2['SCoordinates'].apply(lambda x: x.split()[0][0:-1])
df2['s_lon'] = df2['SCoordinates'].apply(lambda x: x.split()[-1])
df2['d_lat'] = df2['ECoordinates'].apply(lambda x: x.split()[0][0:-1])
df2['d_lon'] = df2['ECoordinates'].apply(lambda x: x.split()[-1])
df2.drop(['SCoordinates','ECoordinates'],axis=1,inplace=True)
df2.to_csv('check.csv',index=False, sep=',', header= True, encoding= 'utf-8', date_format= int)
#print(df2.head())