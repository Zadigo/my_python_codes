#%%
import pandas
import numpy

#%%
# data = pandas.read_csv('https://raw.githubusercontent.com/Zadigo/open-data-party/master/vol_olympics_2016.csv', sep=',')
data = pandas.read_csv('D:\\Programs\\Python\\repositories\\python_codes\\algorithms\\test.csv', sep=',')

#%%
columns=['height', 'weight', 'spike', 'block', 'position_number']
df = pandas.DataFrame(data=data, columns=columns)
df=df[df['spike']!=0]

#%%
# Data analysis
# df.groupby(by=['position_number'])['height'].count()
# df[df['position_number']==4].mean()

#%%
# from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, confusion_matrix

#%%
X = df[['height', 'weight', 'spike', 'block']]
y = df['position_number']

#%%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.7)

# %%
# model = DecisionTreeClassifier(criterion='gini', random_state=42)
model = KNeighborsClassifier(1, weights='uniform')

#%%
model.fit(X_train, y_train)

# %%
model.score(X_train, y_train)
# predictions = model.predict(X_test)
# predictions[:10]
# observations = [[178]]
# prediction = model.predict(observations)
# prediction

#%%
X_test[:10]

#%%
# Test model accuracy
# y_test_array = [v for v in y_test[:5]]
# y_test_array = numpy.asarray(y_test)
mean_absolute_error(y_test, predictions)
# confusion_matrix(y_test, predictions)

#%%
# df.ix[55]
# data[50:56]
