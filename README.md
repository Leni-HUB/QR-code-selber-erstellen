# QR-Code Generator

Ein einfaches Python-Programm mit einer grafischen Benutzeroberfläche (GUI) zur Erstellung von QR-Codes. Der generierte QR-Code wird als Bild gespeichert.

## Anforderungen

Stelle sicher, dass folgende Python-Bibliotheken installiert sind:

```sh
pip install qrcode[pil] tkinter pillow
```

## Funktionsweise

1. Benutzer gibt eine URL oder einen Text ein.
2. Benutzer gibt einen Namen für die Bilddatei ein.
3. Das Programm erstellt den QR-Code und speichert ihn im Ordner `Bilder QR-code`.

## Verwendung

Führe das Skript mit folgendem Befehl aus:

```sh
python scriptname.py
```

Dabei ist `scriptname.py` durch den tatsächlichen Namen der Python-Datei zu ersetzen.

## Ordnerstruktur

Nach der ersten Generierung wird automatisch ein Ordner erstellt:

```
Projektordner/
├── scriptname.py
├── Bilder QR-code/
│   ├── beispiel.png
│   ├── weiteres_beispiel.png
```

