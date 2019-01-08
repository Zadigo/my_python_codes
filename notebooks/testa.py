#%%
import pandas

#%%
data=pandas.read_csv('C:\\Users\\Pende\\Documents\\Python\\notebooks\\testa.csv', sep=';', parse_dates=['date'])

#%%
columns=['nom','prenom','date','statut','score']
df=pandas.DataFrame(data=data, columns=columns)

#%%
new_df=df[['date','statut']]
new_df.groupby(by='statut')['statut'].count()

#%%
# new_df.dtypes
a=new_df['statut'].apply(lambda x: x.replace('Ingénieur','1')).apply(lambda x: x.replace('Docteur','2'))
new_df['enc_statut']=a
new_df.drop(columns=['statut'],inplace=True)

#%%
def convert_percentage(val):
    if val == 'Ingénieur':
        return 1
    else:
        return 2
# p=df['statut'].apply(convert_percentage).astype('float')
p=df['statut'].apply(convert_percentage).astype('int')

#%%
total_score = df['score'].sum()
def pct_on_total(val):
    return val/total_score
pct=df['score'].apply(pct_on_total).astype('float')
df['pct_on_total']=pct

#%%
replace_date=df['date']
def change_date(val):
    new_date=pandas.datetime.strptime(val,'%d-%m-%Y')
    return new_date
df['date'].apply(change_date)

#%%
# df.groupby('date')['score'].transform('mean')
# df['total_scores']=df['score']/df['score'].sum()
# y=df.groupby(by=['date', pandas.Grouper(key='date', freq='M')])['score'].mean()
# df['score'].agg({'score':['sum', 'mean']})
df