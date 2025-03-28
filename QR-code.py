import os
import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def erstelle_qr_code_gui():
    def generiere_qr_code():
        # Link und Bildname aus den Eingabefeldern holen
        link = link_entry.get()
        bild_name = bildname_entry.get()

        if not link:
            messagebox.showerror("Fehler", "Bitte gib einen Link ein.")
            return
        if not bild_name:
            messagebox.showerror("Fehler", "Bitte gib einen Namen für das Bild ein.")
            return

        # Ordnerpfad relativ zur Position der Python-Datei
        ordner_pfad = os.path.join(os.path.dirname(__file__), "Bilder QR-code")
        if not os.path.exists(ordner_pfad):
            os.makedirs(ordner_pfad)

        # QR-Code generieren
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        qr.make(fit=True)

        # QR-Code als Bild speichern
        img = qr.make_image(fill_color="black", back_color="white")
        bild_pfad = os.path.join(ordner_pfad, f"{bild_name}.png")
        img.save(bild_pfad)

        # Erfolgsmeldung anzeigen
        messagebox.showinfo("Erfolg", f"QR-Code wurde erfolgreich als '{bild_pfad}' gespeichert.")
        link_entry.delete(0, tk.END)
        bildname_entry.delete(0, tk.END)

    # Hauptfenster erstellen
    root = tk.Tk()
    root.title("QR-Code Generator")
    root.geometry("400x300")
    root.resizable(False, False)

    # GUI-Elemente
    tk.Label(root, text="QR-Code Generator", font=("Arial", 16)).pack(pady=10)

    tk.Label(root, text="Link eingeben:").pack(anchor="w", padx=20)
    link_entry = tk.Entry(root, width=40)
    link_entry.pack(pady=5)

    tk.Label(root, text="Bildname eingeben:").pack(anchor="w", padx=20)
    bildname_entry = tk.Entry(root, width=40)
    bildname_entry.pack(pady=5)

    generate_button = tk.Button(root, text="QR-Code generieren", command=generiere_qr_code, bg="Gray", fg="white")
    generate_button.pack(pady=20)

    # Hauptfenster starten
    root.mainloop()

if __name__ == "__main__":
    erstelle_qr_code_gui()