
import streamlit as st

st.title("Window of Tolerance")

st.write("""
Deze app helpt je begrijpen wat er in je lichaam gebeurt bij stress en trauma.
Het lichaam kan denken dat het gevaar nog steeds aanwezig is.
""")

state = st.radio(
    "Hoe voel je je nu?",
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
    st.error("Je zenuwstelsel staat op alarm.")
    st.write("Klachten kunnen zijn: onrust, angst, spanning, hartkloppingen.")

elif state == "Onderprikkeld / afgesloten (hypoarousal)":
    st.warning("Je zenuwstelsel is afgevlakt of afgesloten.")
    st.write("Klachten kunnen zijn: leegte, vermoeidheid, dissociatie.")
