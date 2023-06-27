from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apply')
def index():
    return render_template('apply.html')

@app.route('/list')
def index():
    return render_template('list.html')



if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000", debug =True)