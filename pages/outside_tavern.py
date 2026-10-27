import streamlit as st

st.write("You walk outside and are immediately surrounded by the chirping of crickets. The moon has risen full in the sky above your head and the stars are twinkling faintly above.")

if "star_lore" not in st.session_state:
    st.session_state.star_lore = False


if not st.session_state.star_lore:
    if st.button("Recall a story your grandmother once told you."):
        st.write("*Lore Unlocked!*")
        st.session_state.star_lore = True

        st.write("A memory hits you out of nowhere, and you are transported back to the old wooden floor in your grandmother's hut as she tells you a story." \
        "'The people believed for many years that when they die, they become stars and look down upon their loved ones in the living world,' she says. 'So whenever you're feeling sad or lonely, look up and count all the stars. They are all the ones who came before you and are watching over you now.'")

        st.button("You were amazed by the story.")
        st.button("You did not quite believe everything your grandmother was saying.")

if st.button("You decide to go for a walk."):
    st.text("walky walky time :)")
