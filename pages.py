import streamlit as st

#rooms found

rooms = ["hallwayFound", "outsideFound", "forestFound", "clearingFound", "bedroomFound", "caveFound", "bigTreeFound"]

for room in rooms:
    if room not in st.session_state:
        st.session_state[room] = False


tavern = st.Page("pages/tavern.py", title = "Tavern", icon = "🍺", default = True)
upstairs_hallway = st.Page("pages/upstairs_hallway.py", title = "Hallway")
outside_tavern = st.Page("pages/outside_tavern.py", title = "Outside")
forest = st.Page("pages/forest.py", title = "A Quiet Forest")
clearing = st.Page("pages/clearing.py", title = "An Empty Forest Clearing")
bedroom = st.Page("pages/bedroom.py", title = "Bedroom")
big_tree = st.Page("pages/big_tree.py", title = "A Very Big Tree")
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

st.navigation(visible).run()
