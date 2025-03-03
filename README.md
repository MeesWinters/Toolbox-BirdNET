
# De Bio-Informatica Toolbox
Mees Winters | 436369 | 20245-2025
___

### About
Birdnet analyzer is een tensorflow model getraind om vogelzang te herkennen. 
Normaal is deze tool te gebruiken. Deze website is gemaakt als gebruiksvriendelijker alternatief voor de command line tool.
Met de website kan een geluidsopname geanalyseerd worden en word een overzicht gegeven. Voor gebruik van de website zie de ***use*** pagina op de website.

### installatie

Voor installatie worden twee git repositories gebuikt. Installeer eerst de GUI met:

> git clone https://github.com/MeesWinters/Toolbox_birdNET.git
>

move in de folder

> cd Toolbox_birdNET
> 

Installeer in de deze folder BirdNet-analyzer

> git clone https://github.com/kahst/BirdNET-Analyzer.git
> 

Activeer de venv 

> source Toolbox_venv/bin/activate
> 
 
Test of de BirdNET-Analyzer werkt

> python -m BirdNET-Analyzer/birdnet_analyzer.analyze

Mocht dit nog niet werken, download dan alle dependicies opnieuw
> pip install -r Birdnet-Analyzer/requirements.txt



