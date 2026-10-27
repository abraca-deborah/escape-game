import streamlit as st


st.write("You're standing in a tavern, with no recollection of who you were or how you got here.")
st.write("What do you do?")

if st.button("Take a closer look at what you're carrying."):
    st.write("*Inventory unlocked!*")
    st.write("You are carrying " + st.session_state.you.inventory)

if st.button("Look around at the tavern."):
    st.write("The tavern is pretty empty. There's only a few other customers in here besides you, and they all appear to be minding their own business.\nThe bartender hums quietly to themself as they wipe down one of the counters. In the corner, the neon sign begins to flicker.")

if not st.session_state.you.set:
    if st.button("Find a mirror."):
        st.write("There's a dingy mirror in the corner. You take a look at yourself in it.")

        st.session_state.you.setEyes(st.text_input("Your eyes are the color ", value = st.session_state.you.eyeColor))
        st.session_state.you.setHair(st.text_input("Your hair is the color ", value = st.session_state.you.hairColor))
        st.session_state.you.setHairLength(st.text_input("Your hair is (length)", value = st.session_state.you.hairLength))

        if st.button("You've finished looking at yourself."):
            st.session_state.you.set = True
            st.rerun()




#after a bit more exploring

if st.button("Head up the stairs."):
    if st.session_state.hallwayFound == False:
        st.write("*New Area Unlocked: Hallway!*")
    st.session_state.hallwayFound = True
    st.switch_page("pages/upstairs_hallway.py")

#or

if st.button("Go outside."):
    if st.session_state.outsideFound == False:
        st.write("*New Area Unlocked: Outside the Tavern!*")
    st.session_state.outsideFound = True
    st.switch_page("pages/outside_tavern.py")

