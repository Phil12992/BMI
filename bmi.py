import tkinter as tk
from tkinter import ttk

def berechne_bmi(event=None):
    große_cm = slider_groesse.get()
    gewicht_kg = slider_gewicht.get()
    alter = slider_alter.get()

    große_m = große_cm / 100
    bmi = gewicht_kg / (große_m ** 2)
    bmi_gerundet = round(bmi, 2)

    # Werte anzeigen
    label_ergebnis.config(text=f"Dein BMI beträgt: {bmi_gerundet}")
    label_groesse_wert.config(text=f"{int(große_cm)} cm")
    label_gewicht_wert.config(text=f"{int(gewicht_kg)} kg")
    label_alter_wert.config(text=f"{int(alter)} Jahre")

    # BMI-Bewertung je Altersgruppe
    if alter < 18:
        kategorie = "BMI unter 18 wird individuell bewertet."
    else:
        if 18 <= alter <= 29:
            if bmi < 18.5:
                kategorie = "Du hast Untergewicht."
            elif 18.5 <= bmi < 24.9:
                kategorie = "Du hast Normalgewicht."
            elif bmi >= 24.9:
                kategorie = "Du hast Übergewicht."
        elif 30 <= alter <= 39:
            if bmi < 19:
                kategorie = "Du hast Untergewicht."
            elif 19 <= bmi < 25.5:
                kategorie = "Du hast Normalgewicht."
            elif bmi >= 25.5:
                kategorie = "Du hast Übergewicht."
        elif 40 <= alter <= 49:
            if bmi < 20:
                kategorie = "Du hast Untergewicht."
            elif 20 <= bmi < 26:
                kategorie = "Du hast Normalgewicht."
            elif bmi >= 26:
                kategorie = "Du hast Übergewicht."
        elif 50 <= alter <= 59:
            if bmi < 21:
                kategorie = "Du hast Untergewicht."
            elif 21 <= bmi < 27:
                kategorie = "Du hast Normalgewicht."
            elif bmi >= 27:
                kategorie = "Du hast Übergewicht."
        elif 60 <= alter <= 69:
            if bmi < 22:
                kategorie = "Du hast Untergewicht."
            elif 22 <= bmi < 28:
                kategorie = "Du hast Normalgewicht."
            elif bmi >= 28:
                kategorie = "Du hast Übergewicht."
        elif alter >= 70:
            if bmi < 22:
                kategorie = "Du hast Untergewicht."
            elif 22 <= bmi < 29:
                kategorie = "Du hast Normalgewicht."
            elif bmi >= 29:
                kategorie = "Du hast Übergewicht."

    label_kategorie.config(text=kategorie)

# Fenster erstellen
fenster = tk.Tk()
fenster.title("BMI Rechner")
fenster.geometry("360x480")
fenster.resizable(False, False)

# Titel
label_titel = ttk.Label(fenster, text="BMI Rechner", font=("Helvetica", 16, "bold"))
label_titel.pack(pady=10)

# Alter
label_alter = ttk.Label(fenster, text="Alter:")
label_alter.pack()
slider_alter = ttk.Scale(fenster, from_=10, to=100, orient="horizontal", command=berechne_bmi)
slider_alter.set(25)
slider_alter.pack(fill="x", padx=20)
label_alter_wert = ttk.Label(fenster, text="25 Jahre")
label_alter_wert.pack()

# Größe
label_groesse = ttk.Label(fenster, text="Körpergröße:")
label_groesse.pack()
slider_groesse = ttk.Scale(fenster, from_=100, to=220, orient="horizontal", command=berechne_bmi)
slider_groesse.set(170)
slider_groesse.pack(fill="x", padx=20)
label_groesse_wert = ttk.Label(fenster, text="170 cm")
label_groesse_wert.pack()

# Gewicht
label_gewicht = ttk.Label(fenster, text="Gewicht:")
label_gewicht.pack(pady=(10, 0))
slider_gewicht = ttk.Scale(fenster, from_=30, to=150, orient="horizontal", command=berechne_bmi)
slider_gewicht.set(70)
slider_gewicht.pack(fill="x", padx=20)
label_gewicht_wert = ttk.Label(fenster, text="70 kg")
label_gewicht_wert.pack()

# BMI-Ausgabe
label_ergebnis = ttk.Label(fenster, text="Dein BMI beträgt: ", font=("Helvetica", 13, "bold"))
label_ergebnis.pack(pady=15)

# Gewichtskategorie
label_kategorie = ttk.Label(fenster, text="", font=("Helvetica", 12))
label_kategorie.pack()

# Initialberechnung
berechne_bmi()

# Fenster starten
fenster.mainloop()

# Fenster starten
fenster.mainloop()



