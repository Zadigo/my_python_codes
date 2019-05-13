import flask

app=flask.Flask(__name__)

@app.route('/')
def test():
    return 'test'

def show(function1, w):
    def _dec(function2):
        print(function2(), w + w)
        print(function1(), w * 4)
    return _dec
    
def e():
    return 'Two + Two ='

@show(e, 1)
def example():
    return 'One + One = '
    
example
