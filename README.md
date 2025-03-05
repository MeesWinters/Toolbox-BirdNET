
# De Bio-Informatica Toolbox
Mees Winters | 436369 | 2024-2025 | Versie 0.1
___

### About
Birdnet analyzer is een tensorflow model getraind om vogelzang te herkennen. 
Normaal is deze tool te gebruiken via de command line. Deze website is gemaakt als gebruiksvriendelijker alternatief voor de command line tool.
Met de website kan een geluidsopname geanalyseerd worden en word een overzicht gegeven. Voor gebruik van de website zie de ***use*** pagina op de website.

___

### installatie

Voor installatie worden twee git repositories gebuikt. Installeer eerst de GUI met:
> git clone https://github.com/MeesWinters/Toolbox_birdNET.git

move in de folder
> cd Toolbox_birdNET

Installeer in de deze folder BirdNet-analyzer
> git clone https://github.com/kahst/BirdNET-Analyzer.git

Maak een virtual environment en activeer deze (optioneel)
> python -m venv /path/naar/venv
> 
> source /path/naar/venv

Installeer alle nodige python packages
> pip install -r Birdnet-Analyzer/requirements.txt

Test BirNET-Analyzer
>python -m BirdNET-Analyzer/birdnet_analyzer.analyze

___

### Support

Voor verdere hulp bij installatie van BirdNET-analyzer de github repository geraadpleegd worden. Hier is o.a. een installatie guide te vinden

https://github.com/kahst/BirdNET-Analyzer

Voor vragen over gebruik van de website kunnen vragen gesteld worden via

***m.a.winters@st.hanze.nl***
