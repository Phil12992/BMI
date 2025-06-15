import streamlit as st

st.set_page_config(page_title="BMI Rechner", layout="centered")
st.title("🧮 BMI Rechner")

# Eingabefelder
alter = st.slider("Alter", 10, 100, 25)
groesse = st.slider("Körpergröße (cm)", 100, 220, 170)
gewicht = st.slider("Gewicht (kg)", 30, 150, 70)

# BMI berechnen
bmi = gewicht / ((groesse / 100) ** 2)
bmi_gerundet = round(bmi, 2)
st.markdown(f"### Dein BMI beträgt: **{bmi_gerundet}**")

# Bewertung nach Alter
def bewerte_bmi(bmi, alter):
    if alter < 18:
        return "🔶 BMI unter 18 wird individuell bewertet."
    elif alter <= 29:
        return "🟢 Normalgewicht" if 18.5 <= bmi < 24.9 else "🔴 Übergewicht" if bmi >= 24.9 else "🔵 Untergewicht"
    elif alter <= 39:
        return "🟢 Normalgewicht" if 19 <= bmi < 25.5 else "🔴 Übergewicht" if bmi >= 25.5 else "🔵 Untergewicht"
    elif alter <= 49:
        return "🟢 Normalgewicht" if 20 <= bmi < 26 else "🔴 Übergewicht" if bmi >= 26 else "🔵 Untergewicht"
    elif alter <= 59:
        return "🟢 Normalgewicht" if 21 <= bmi < 27 else "🔴 Übergewicht" if bmi >= 27 else "🔵 Untergewicht"
    elif alter <= 69:
        return "🟢 Normalgewicht" if 22 <= bmi < 28 else "🔴 Übergewicht" if bmi >= 28 else "🔵 Untergewicht"
    else:
        return "🟢 Normalgewicht" if 22 <= bmi < 29 else "🔴 Übergewicht" if bmi >= 29 else "🔵 Untergewicht"

kategorie = bewerte_bmi(bmi, alter)
st.write(f"**Kategorie:** {kategorie}")

