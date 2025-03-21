from flask import Flask, render_template, url_for, request
from werkzeug.utils import secure_filename

upload_folder = "static/files"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config["UPLOAD_FOLDER"] = upload_folder

@app.route("/", methods=['POST', 'GET'])
def use():
    if request.method == "GET":
        return render_template("get.html")

    elif request.method == "POST":

        f = request.files['file']
        f.save("static/files/" + secure_filename(f.filename))

        kwargs = {
            'lengtegraad':  request.form['lengtegraad'],
            'breedtegraad': request.form['breedtegraad'],
            'gevoeligheid': request.form['gevoeligheid'],
            'zekerheid': request.form['zekerheid'],
        }

        return render_template("post.html", **kwargs)

@app.route("/howto.html")
def how_to():
    return render_template("howto.html")


@app.route("/about.html")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)