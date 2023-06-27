from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apply')
def apply():
    return render_template('apply.html')

@app.route('/list')
def list():
    return render_template('list.html')

@app.route('/applyphoto')
def applyphoto():
    location = request.args.get("location")
    cleaness = request.args.get("clean")
    builtin = request.args.get("built")
    print(location, cleaness, builtin)
    return render_template('apply_photo.html')

@app.route('/upload_done', methods=["POST"])
def upload_done():
    uploaded_files = request.files["file"]
    uploaded_files.save("static/img/{}.jpeg".format(1))

    return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000", debug =True)