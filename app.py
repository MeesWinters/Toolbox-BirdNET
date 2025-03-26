from flask import Flask, render_template, request
from werkzeug.utils import secure_filename


from inputprocess import analyze, emptydir


upload_folder = "static/files"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config["UPLOAD_FOLDER"] = upload_folder



@app.route("/", methods=['POST', 'GET'])
def use():
    if request.method == "GET":
        return render_template("get.html")

    elif request.method == "POST":

        emptydir()

        f = request.files['file']
        filepath = "static/files/" + secure_filename(f.filename)
        f.save(filepath)

        a = analyze(filepath)
        analyze.graph(a)

        emptydir()

        return render_template("post.html")

@app.route("/howto.html")
def how_to():
    return render_template("howto.html")


@app.route("/about.html")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)