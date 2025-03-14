from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def use():
    if request.method == "GET":
        return render_template("frontpage.html")

    elif request.method == "POST":
        print('de post is er')
        kwargs = {
            'lengtegraad':  request.form['lengtegraad'],
            'breedtegraad': request.form['breedtegraad'],
            'gevoeligheid': request.form['gevoeligheid'],
            'zekerheid': request.form['zekerheid'],
        }
        return render_template("output.html", **kwargs)
@app.route("/howto.html")
def how_to():
    return render_template("howto.html")

@app.route("/about.html")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)