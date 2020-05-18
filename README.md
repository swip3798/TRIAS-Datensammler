# TRIAS-Datensammler

## Vorbereitung
Zunächst muss eine `sensitive.py` Datei erstellt werden (siehe `sensitive.py.example`). In dieser müssen die TRIAS-Url, der TRIAS-Zugangsschlüssel sowie die SQLAlchemy-URL festgelegt werden. Darüber hinaus wird eine laufende Datenbank-Instanz benötigt. Hier kann im Grunde jedes mit SQLAlchemy kompatible DBMS genutzt werden, jedoch getestet wurde dieser Datensammler ausschließlich mit MySQL.

## Nutzung mit Docker (Empfohlen)

Die einfachste Nutzung des Datensammlers ist über Docker. 

```
git clone https://github.com/swip3798/TRIAS-Datensammler.git
cd TRIAS-Datensammler
docker build -t triasminer .
docker run -it -d triasminer
```

## Manuelle Nutzung
Für die manuelle Nutzung muss vorab der jeweilige Python Treiber für das gewünschte DBMS installiert werden. Anschließend kann der Datensammler gestartet werden.

```
git clone https://github.com/swip3798/TRIAS-Datensammler.git
cd TRIAS-Datensammler
pip install -r requirements.txt
python main.py
```
Der Datensammler frägt nun nacheinander alle Haltestellen nach verfügbaren Halten ab und zeichnet Änderungen in der Datenbank auf.
Mit STRG+C kann der Datensammler gestoppt werden.

## Timeslot Service
Zur Überwachung des Zustands des Timeslot Services wird beim Start des Datensammlers eine REST-API unter [http://localhost:7777/timeslots](http://localhost:7777/timeslots) verfügbar gemacht, bei dem die aktuell vergebenen Timeslots angezeigt werden. So kann ein Überlaufen der Timeslots bei vielen Halten vermieden werden.