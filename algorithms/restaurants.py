#%%
import pandas
import datetime
from pandas import read_csv
from pandas import DataFrame

data = read_csv('C:\\Users\\Zadigo\\Documents\\Programs\\my_python_codes\\restaurants.csv', parse_dates=True)
columns = ['vente', 'supreme', 'date', 'heure']
df = DataFrame(data, columns=columns)

#%%
df['pct'] = df['supreme']/df['vente']
df['date'] = pandas.to_datetime(df['date'])
df['timestamp'] = df['date'].apply(lambda x: datetime.datetime.timestamp(x))

#%%
df.groupby(by=['supreme'])['vente'].sum()


#%%
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = df[['timestamp']]
y = df['vente']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25)
print(X_train)
model = LinearRegression()
model.fit(X_train, y_train)

observations = [[145]]
prediction = model.predict(observations)
prediction
