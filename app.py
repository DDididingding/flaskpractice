from flask import Flask, render_template, request, redirect, url_for
import sys, database

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apply')
def apply():
    return render_template('apply.html')

@app.route('/list')
def list():
    house_list = database.load_list()
    length = len(house_list)

    return render_template('list.html', house_list = house_list, length = length)

@app.route('/applyphoto')
def applyphoto():
    location = request.args.get("location")
    cleaness = request.args.get("clean")
    builtin = request.args.get("built")
    if cleaness == None:
        cleaness = False
    else:
        cleaness = True

    database.save(location, cleaness, builtin)
    return render_template('apply_photo.html')

@app.route('/upload_done', methods=["POST"])
def upload_done():
    uploaded_files = request.files["file"]
    uploaded_files.save("static/img/{}.jpeg".format(database.now_index()))

    return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000", debug =True)