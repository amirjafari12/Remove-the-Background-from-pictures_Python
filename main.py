"""Mit diesen Python Library kann man durch einpaar codes den Hintergrund eines Bildes ganzeinfach entfernen.
Zuerst muss man mit dem Befehl pip install rembg den library herunter laden und von diesen vom PIL Ordner den Image Funktion importieren."""

import rembg
from PIL import Image

input_path = "Der Name des Bildes"
output_path = "Der Name des Bildes, wie es heißen soll, nach dem der Hintergrund entfernt wurde"
input_image = Image.open(input_path)
output_image = rembg.remove(input_image)
output_image.save(output_path)
