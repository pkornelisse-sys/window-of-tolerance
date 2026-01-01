import streamlit as st

st.set_page_config(page_title="Window of Tolerance", layout="centered")

st.title("Window of Tolerance")

st.write("""
Deze app is **geen oefening**.  
Geen oplossing.  
Alleen **zien en begrijpen** wat er gebeurt in je lichaam.
""")

st.markdown("---")

st.header("1. Twee systemen in één mens")

st.write("""
Je hebt **twee systemen** die tegelijk werken:

**Het denkende brein**
- weet hoe laat het is  
- weet waar je bent  
- weet dat iets voorbij is  

**Het lichaam / zenuwstelsel**
- scant voortdurend op veiligheid  
- reageert automatisch  
- kent alleen: **veilig / onveilig**
""")

st.markdown("---")

st.header("2. Wat trauma doet met het lichaam")

st.write("""
Bij overweldiging of langdurige onveiligheid leert het lichaam:

> *“Ik moet altijd klaarstaan.”*

De ervaring wordt niet alleen herinnering, maar ook:
- spierspanning  
- ademhaling  
- hartslag  
- reflexen  

Dit gebeurt **zonder woorden**.
""")

st.markdown("---")

st.header("3. Waarom het lichaam denkt dat het 'daar nog is'")

st.write("""
In het **heden** gebeurt iets kleins:
- een toon  
- een blik  
- een situatie  
- een gevoel  

Het lichaam herkent dit als *gevaar*  
en reageert alsof het **nu** gebeurt.
""")

st.markdown("---")

st.header("4. Geen tijdsbesef in het lichaam")

st.write("""
Het denkende brein werkt met:
- toen  
- nu  
- straks  

Het lichaam werkt met:
- veilig  
- onveilig  

Daarom kan iets ouds **nu** voelen.
""")

st.markdown("---")

st.header("Hoe voel je je nu?")

state = st.radio(
    "",
    [
        "Binnen mijn tolerantievenster",
        "Overprikkeld (hyperarousal)",
        "Onderprikkeld / afgesloten (hypoarousal)"
    ]
)

if state == "Binnen mijn tolerantievenster":
    st.success("Je bent relatief veilig en aanwezig.")
    st.write("Denken, voelen en handelen zijn in balans.")

elif state == "Overprikkeld (hyperarousal)":
    st.error("Je zenuwstelsel staat op scherp.")
    st.write("Mogelijk: onrust, spanning, alertheid, angst.")

elif state == "Onderprikkeld / afgesloten (hypoarousal)":
    st.warning("Je zenuwstelsel heeft zich teruggetrokken.")
    st.write("Mogelijk: leegte, afstand, verdoving.")

st.markdown("---")

st.write("""
