import subprocess
import os
from matplotlib import pyplot as plt
import pandas
from flask import request


class analyze():
    def __init__(self, file):

        self.file = file
        filepath = "../" + file
        subprocess_args = ["python3", "-m", "birdnet_analyzer.analyze", filepath, "-o", "../static/files/", "--rtype", "csv"]
        print(type(subprocess_args))

        if request.form['week'] != '' :
            self.week = request.form['week']
            subprocess_args = subprocess_args + ["--week", str(self.week)]
        if request.form['breedtegraad'] != '' :
            self.breedtegraad = request.form['breedtegraad']
            subprocess_args = subprocess_args + ["--lat", str(self.breedtegraad)]
        if request.form['lengtegraad'] != '' :
            self.lengtegraad = request.form['lengtegraad']
            subprocess_args = subprocess_args + ["--lon", str(self.lengtegraad)]
        if request.form['gevoeligheid'] != '' :
            self.gevoeligheid = request.form['gevoeligheid']
            subprocess_args = subprocess_args + ["--sensitivity", str(self.gevoeligheid)]
        if request.form['zekerheid'] != '' :
            self.zekerheid = request.form['zekerheid']
            subprocess_args = subprocess_args + ["--min_conf", str(self.zekerheid)]
            print(subprocess_args)

        subprocess.run(subprocess_args, cwd="BirdNET-Analyzer")

    def graph(self):
        outpath = self.file.split(".")[0] + ".BirdNET.results.csv"
        data = pandas.read_csv(outpath)
        df = pandas.DataFrame(data)

        X = list(df.iloc[:,0])
        Y = list(df.iloc[:,1])

        plt.bar(X ,Y, color="g")
        plt.show()

        return


def emptydir():
    files = os.listdir("static/files")
    for file in files:
        fp = os.path.join("static/files", file)
        if os.path.isfile(fp):
            os.remove(fp)
    return

def main():
    return

if __name__ == '__main__':
    main()