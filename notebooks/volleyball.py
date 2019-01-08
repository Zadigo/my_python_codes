#%%
import pandas
import datetime

#%%
data = pandas.read_csv('https://raw.githubusercontent.com/Zadigo/open-data-party/master/vol_olympics_2016.csv')

#%%
df = pandas.DataFrame(data=data)

#%%
def get_age(value):
    player_year = datetime.datetime.strptime(str(value), '%d/%m/%Y').year
    return datetime.datetime.now().year - player_year

df['current_age']=df['date_of_birth'].apply(get_age)

#%%
df.describe()

#%%
df['height'].aggregate(['mean','min','max'])

#%%
df[df['spike']!=0].describe()

#%%
df.groupby(by=['position_number'])['height', 'spike', 'block'].mean()

#%%
df.groupby(by=['position_number'])['height'].count()

#%%
df.groupby(by=['country'])['height'].std()

#%%
df.groupby(by=['height'])['position_number'].count()
