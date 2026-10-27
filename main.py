import streamlit as st
from Player import Player


st.title("A Dark and Stormy Night")

if "you" not in st.session_state:
    st.session_state.you = Player("brown","brown","medium")


#here we are setting visible rooms
rooms = ["hallwayFound", "outsideFound", "forestFound", "clearingFound", "bedroomFound", "caveFound", "bigTreeFound"]
for room in rooms:
    if room not in st.session_state:
        st.session_state[room] = False

#and here we are setting up the rooms that are pages
tavern = st.Page("pages/tavern.py", title = "Tavern", icon = "🍺", default = True)
upstairs_hallway = st.Page("pages/upstairs_hallway.py", title = "Hallway")
outside_tavern = st.Page("pages/outside_tavern.py", title = "Outside the Tavern")
forest = st.Page("pages/forest.py", title = "A Quiet Forest")
clearing = st.Page("pages/clearing.py", title = "An Empty Forest Clearing")
bedroom = st.Page("pages/bedroom.py", title = "Bedroom")
big_tree= st.Page("pages/big_tree.py", title = "A Very Big Tree")
cave = st.Page("pages/cave.py", title = "A Mysterious Cave")

visible = [tavern]

if st.session_state.hallwayFound:
    visible.append(upstairs_hallway)
if st.session_state.outsideFound:
    visible.append(outside_tavern)
if st.session_state.forestFound:
    visible.append(forest)
if st.session_state.clearingFound:
    visible.append(clearing)
if st.session_state.bedroomFound:
    visible.append(bedroom)
if st.session_state.bigTreeFound:
    visible.append(big_tree)
if st.session_state.caveFound:
    visible.append(cave)

st.navigation(visible).run()


