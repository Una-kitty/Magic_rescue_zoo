
import streamlit as st
import random


st.title("Magic Pet Rescue")
st.write("Help lost baby animals and bring them home!")

if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.pets_rescued = []
    st.session_state.energy = 100
    st.session_state.game_stage = "start"
    
def reset_game():
    st.session_state.score = 0
    st.session_state.pets_rescued = []
    st.session_state.energy = 100
    st.session_state.game_stage = "start"

# start screeen
if st.session_state.game_stage == "start":
    name = st.text_input("your rescuer name?", "lil rescue dude")
    
    
    if st.button("Start Exploring"):
        st.session_state.player_name = name
        st.session_state.game_stage = "explore"
        
        
# Explore Screen
elif st.session_state.game_stage == "explore":
    st.write("You are walking in the forest...")
    st.write("Energy:", st.session_state.energy)
    
    
    if st.button("search for lost animal"):
        animals = ["Baby Bunny", "Tiny Fox", "Fluffy Kitten", "Baby Panda", "Little Penguin", "cute monkey", "baby hamster"]
        st.session_state.current_animal = random.choice(animals)
        st.session_state.energy = st.session_state.energy - 15
        st.session_state.game_stage = "rescue"
        
# Rescue screen
elif st.session_state.game_stage == "rescue":
    animal = st.session_state.current_animal
    st.write("You found a", animal, "!")
    
    if st.button("Help the animal"):
        st.write("You found a", animal, "!")
        st.session_state.pets_rescued.append(animal)
        st.session_state.score = st.session_state.score + 20
        st.session_state.game_stage = "explore"
        
  
## show score always
st.write("---")
st.write("Animals rescued:", len(st.session_state.pets_rescued))   
st.write("Total Points:", st.session_state.score)

 
if st.button("Restart Game"):
    reset_game()
    

st.markdown('<p style="text-align:center; font-family:VT323, monospace;"> made by Valen from Repton with love</p >', unsafe_allow_html=True)

