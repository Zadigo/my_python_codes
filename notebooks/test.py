#%%
import pandas
import matplotlib

#%%
data = pandas.read_csv('C:\\Users\\Pende\\Documents\\Python\\notebooks\\transpole.csv')
columns = ['Type de véhicule', 'Modèle','Date de mise en service']
df = pandas.DataFrame(data=data, columns=colums, parse_dates=True)

#%%
renamed = df.rename(columns={
    'Type de véhicule':'type',
    'Modèle':'model',
    'Date de mise en service':'first_service'
})
# df.head(n=5)
# df['Modèle']
# df[['Modèle','Type de véhicule']]
# df['Modèle'].value_counts()
# df['Modèle'].value_counts().plot(kind='bar')
# irisbus = df[df['Type de véhicule'] == 'STANDARD']
# irisbus[:15]

# irisbus = df['Type de véhicule'] == 'STANDARD'
# model = df['Modèle'] == 'BUS AGORA 2'
# [irisbus & model][:15]

#%%
# seulement_les_modeles = df[['Modèle']].copy()
renamed.first_service[:5]

#%%
# renamed.groupby(by='model')['model'].count()
# df.loc[5:15]
# df.iloc[5:15]
