import flask


# e = types.ModuleType('test')
# e.__file__='rest'
# print(e)

# with open('C:\\Users\\Zadigo\\Documents\\Programs\\my_python_codes\\exercises\\test4.py', mode='rb') \
#         as config_file:
#         exec(compile(config_file.read(1024), 'test', 'exec'), {})
#         print(config_file)

app=flask.Flask(__name__)

app.config