import subprocess
import os
from flask import request

from matplotlib import pyplot as plt
import pydub

"""
Dit script bevat verschillende functies die worden gebruikt voor de analyze van het audio bestand. 

Author: Mees Winters
Date: April 2025
"""


class analyze():
    """
    Bevat functies voor het analyseren van audio en het verwerken van de data.
    """
    def __init__(self, file):
        """
        Args:
            file: Audio bestand met opname vogelzang

        __init__ maakt gebruik van subprocess om zo de opname mee te geven aan BirdNet-Analyzer.
        """

        self.file = file
        filepath = "../" + file

        #standaard argumenten voor subprocess, onafhankelijk van parameters gegeven door gebruiker
        subprocess_args = ["python3", "-m", "birdnet_analyzer.analyze", filepath, "-o", "../static/files/", "--rtype", "csv"]

        #Als een argument is gegeven in het formulier door de gebruiker, wordt dit hier toegevoegd aan de argumenten voor subprocess
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

        #Analyze van audio
        print(f"\n\n\n\n\n{subprocess_args}\n\n\n\n\n")
        subprocess.run(subprocess_args, cwd="BirdNET-Analyzer")


    def graph(data):
        """'
        Args:
            Data: dit is het CSV bestand gemaakt door Birdnet-Analyzer

        Deze functie maakt een piechart met een plot van het CSV bestand gemaakt door Birdnet-Analyzer

        Returns: None
        """

        #Telt hoeveel elke vogelsoort is gedecteerd
        species_count = {}
        species_conf = {}
        for line in data.split("\n"):
            if "Start" in line or line == "":
                pass #slaat eerste regel over
            else:
                if not line.split(",")[3] in species_count.keys(): #als het een nieuwe soort is
                    species_count[line.split(",")[3]] = 1
                    species_conf[line.split(",")[3]] = [float(line.split(",")[4])]
                else: # als het geen nieuwe soort is
                    species_count[line.split(",")[3]] += 1
                    species_conf[line.split(",")[3]].append(float(line.split(",")[4]))


        for i in species_conf:
            print(f"\n\n\n\n{i}\n\n\n\n")
            print(f"\n\n\n\n{species_conf[i]}\n\n\n\n")

            print(type(species_conf[i][0]))
            mean = sum(species_conf[i])/len(species_conf[i])
            species_conf[i] = mean


        pieplot(species_count, data)
        barplot(species_conf)

        return


    def audiosplit(data, audiopath):
        """
        Args:
            audiopath: Pad naar audiobestand geupload door gebruiker

        Returns: dict met pad naar audio segmenten en bijpassen data

        Deze functie knipt de audio in verschillende segmenten. Slaat deze segmenten op en slaat het pad op in een dict met bijpassende data
        """

        # pydub gebruikt andere functie voor ander type bestand
        if audiopath.split('.')[-1] == 'mp3':
            audio = pydub.AudioSegment.from_mp3(audiopath)
        elif audiopath.split('.')[-1] == 'wav':
            audio = pydub.AudioSegment.from_wav(audiopath)
        else:
            return


        line_count = 1 #houd bij hoeveelste detectie van een soort het is
        segment_dict = {} #hier wordt het pad naar het segment als key, en de bijpassende soort, start en stop, en zekerheid bijgegeven in song class

        #loop door elke regel in CSV
        for line in data.split("\n"):
            if "Start" in line or line == "":
                pass #slaat eerste regel over
            else:
                #knipt segmenten en geeft pad voor bestand
                segment = audio[float(line.split(",")[0]) * 1000:float(line.split(",")[1]) * 1000]
                species = line.split(",")[3].replace(" ", "_")
                exportpath = "static/files/audiosegments/" + species + str(line_count) + ".mp3"

                #slaat pad naar bestand op met bijpassende data
                segment_dict[exportpath] = song(line)

                #opslaan clip
                segment.export(exportpath, format="mp3")

                line_count += 1

        return segment_dict


class song():
    """"
    Deze functie en class zijn geschreven om alle data die bij een audiofragment hoord op te kunnen slaan
    """
    def __init__(self, line):
        self.start = float(line.split(',')[0])
        self.end = float(line.split(',')[1])
        self.species = line.split(',')[3]
        self.confidence = float(line.split(',')[4])

def barplot(species_conf):
    barplot = plt.bar(species_conf.keys(), species_conf.values(), ec="black")
    plt.bar_label(barplot,labels=species_conf.values(),label_type="edge")
    plt.title("Average confidence per species")
    plt.savefig("static/files/barchart")
    plt.close()

def pieplot(species_count, data):
    plt.pie(species_count.values(), labels=species_count.keys())  # maak chart
    plt.title(f"Species found in {data.split(',')[-1].split('/')[-1]}")  # voegt titel toe met naam van geupload bestand
    plt.savefig("static/files/piechart")
    plt.close()


def emptydir(path = "static/files"):
    """
    Args:
        path: path naar te legen folder

    Deze functie leegt een folder, behalve andere folders. Wordt gebruikt direct na het uploaden van een audio bestand om te zorgen dat data van een vorige analyze niet in de folder zit.

    Returns: None
    """

    files = os.listdir(path)
    for file in files:
        fp = os.path.join(path, file)
        if os.path.isfile(fp):
            os.remove(fp)
    return

def main():
    return

if __name__ == '__main__':
    main()