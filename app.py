from flask import Flask, render_template, request
from werkzeug.utils import secure_filename


from inputprocess import analyze, emptydir

"""
Deze website is gemaakt met gebruik van Flask en Birdnet-Analyzer. De gebruiker kan een bestand uploaden en deze wordt doorgegeven aan Birdnet-Analyzer. 
Er wordt een grafiek gegenereerd met alle detecties en een tabel gemaakt met alle detecties en hun bijpassende audiofragment.

author: Mees Winters
Date: April 2025
"""

upload_folder = "static/files" #geupload audio bestand, csv bestand en grafiek komen in deze folder

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config["UPLOAD_FOLDER"] = upload_folder



@app.route("/", methods=['POST', 'GET'])
def use():
    if request.method == "GET":
        """
        Deze pagina bevat het formulier waarin het audiobestand en extra parameters worden gegeven.
        """
        return render_template("get.html")

    elif request.method == "POST":
        """
        Deze pagina laad wanneer een audio bestand geupload is
        """

        emptydir() #leegt de upload folder
        emptydir("static/files/audiosegments") #leegt de folder met audio segmenten

        #audio bestand opslaan
        f = request.files['file']
        audiopath = "static/files/" + secure_filename(f.filename)
        f.save(audiopath)

        #audio analyseren
        a = analyze(audiopath)
        csvpath = a.file.split('.')[0] + ".BirdNET.results.csv"

        #gegenereerde csv openen en inlezen
        data_open = open(csvpath, 'r')
        data_read = data_open.read()
        data_open.close()

        #data uit csv bestand in grafiek verwerken
        analyze.graph(data = data_read)

        #detecties van vogelzang in aparte fragmenten knippen
        segments = analyze.audiosplit(data = data_read, audiopath = audiopath)

        return render_template("post.html", segments = segments)

@app.route("/howto.html")
def how_to():
    return render_template("howto.html")


@app.route("/about.html")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)