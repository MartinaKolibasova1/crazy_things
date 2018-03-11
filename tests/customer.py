from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)

@app.route('/testing',methods = ['POST'])

def testing():

    test1 = request.form['test']
    r = requests.get('https://api.coinmarketcap.com/v1/ticker/'+test1+'/')
    t = json.loads(r.content)
    for i in range(len(t)):
        return (t[i]['price_usd'])
    #return render_template('testing.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

