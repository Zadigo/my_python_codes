#%%
import pandas
import re

#%%
data = pandas.read_csv('C:\\Users\\Pende\\Documents\\Python\\notebooks\\universites.csv', sep=';')

#%%
columns = ['Annee', 'Diplôme', 'Académie', 'Domaine', 'Discipline', '% de diplômés boursiers', 'Taux de chômage régional', 'Salaire net mensuel médian régional']
df = pandas.DataFrame(data=data, columns=columns)
restructured_df = df.rename(columns={
    'Annee': 'annee',
    'Diplôme': 'diplome',
    'Académie': 'académie',
    'Domaine': 'domaine',
    'Discipline': 'discipline',
    '% de diplômés boursiers': '%boursiers',
    'Taux de chômage régional': '%chomage_region',
    'Salaire net mensuel médian régional': 'salaire_median_region'
})

#%%
restructured_df['salaire_median_region'].astype('int')

#%%
# restructured_df['diplome'].value_counts()
# master_zero = restructured_df[restructured_df['diplome']=='MASTER E0']
# restructured_df.groupby('diplome')['salaire_median_region'].mean()
# restructured_df.groupby('annee')['salaire_median_region'].mean()
# restructured_df[restructured_df['%boursiers']!=0].groupby('annee')['%boursiers'].mean()
# restructured_df[['%boursiers','%chomage_region','salaire_median_region']].agg(['mean'])

#%%
restructured_df[:5]
def _encode_diploma(val):
    if val == 'MASTER LMD':
        return 1
    else:
        return 2
        
encoded_diplomas=restructured_df['diplome'].apply(_encode_diploma)
restructured_df['diplome_enc']=encoded_diplomas
restructured_df[:5]
