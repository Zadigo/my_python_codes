import pandas
import json

# df = pandas.DataFrame(data={'a':[1,5,7,8],'e':[7,9,7,8]})
# df = pandas.DataFrame(data={'a':[1,None,7,8],'e':[7,9,7,8]})

# df2 = df.assign(a=df['a'], e=df['e'], t=lambda x: x['a'] + 15)
# df2 = df.dropna(axis=0)
# df.dropna(axis=0, inplace=True)
# df2 = df.eval('a + e')

path='D:\\Programs\\Repositories\\my_python_codes\\exercises\\test.json'
with open(path, 'r') as f:
    stats = json.load(f)['stats'][0]
    stats.pop('match_stats_id')
    stats.pop('net_approaches')
    stats.pop('odds')
    stats.pop('match')
    df = pandas.DataFrame(data=[stats], columns=['aces','df','tp'])
print(df)