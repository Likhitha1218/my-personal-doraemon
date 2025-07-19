import streamlit as st
import datetime
import random

st.set_page_config(page_title="My Personal Doraemon", page_icon="🐱", layout="centered")

# Animated pastel background
st.markdown("""
<style>
body {
    background: linear-gradient(270deg, #fbeffb, #f0faff, #fefbf1);
    background-size: 600% 600%;
    animation: gradientBG 30s ease infinite;
    font-family: "Comic Sans MS", cursive, sans-serif;
}
@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
</style>
""", unsafe_allow_html=True)

# Stable cartoon images
DORAEMON_URL = "https://raw.githubusercontent.com/yourusername/cartoon-assets/main/doraemon.png"
NOBITA_URL = "https://raw.githubusercontent.com/yourusername/cartoon-assets/main/nobita.png"
SHIZUKA_URL = "https://raw.githubusercontent.com/yourusername/cartoon-assets/main/shizuka.png"
CARTOON_URLS = [
    "https://raw.githubusercontent.com/yourusername/cartoon-assets/main/cartoon1.png",
    "https://raw.githubusercontent.com/yourusername/cartoon-assets/main/cartoon2.png",
    "https://raw.githubusercontent.com/yourusername/cartoon-assets/main/cartoon3.png",
    "https://raw.githubusercontent.com/yourusername/cartoon-assets/main/cartoon4.png",
    "https://raw.githubusercontent.com/yourusername/cartoon-assets/main/cartoon5.png"
]

# Header with Doraemon
col1, col2 = st.columns([1, 8])
with col1:
    st.image(DORAEMON_URL, width=70, use_container_width=True)
with col2:
    st.markdown("<h1 style='font-family:Comic Sans MS;color:#2b2b2b;'>My Personal Doraemon</h1>", unsafe_allow_html=True)

# Date and day with Nobita and Shizuka
today = datetime.datetime.now()
date_str = today.strftime("%d %B %Y")
day_str = today.strftime("%A")
col3, col4, col5, col6 = st.columns([1, 3, 1, 3])
with col3:
    st.image(NOBITA_URL, width=50, use_container_width=True)
with col4:
    st.markdown(f"### {date_str}")
with col5:
    st.image(SHIZUKA_URL, width=50, use_container_width=True)
with col6:
    st.markdown(f"### {day_str}")

# Daily cartoon doodle
today_index = today.timetuple().tm_yday % len(CARTOON_URLS)
st.image(CARTOON_URLS[today_index], caption="Today's Cartoon Doodle", use_container_width=True)

# Advanced Prompt Box for all human needs
st.markdown("## 💬 Doraemon Prompt Box")
user_input = st.text_input("Tell Doraemon how you feel or what you need today:")

if user_input:
    response = ""
    lower_input = user_input.lower()
    if "sad" in lower_input or "depressed" in lower_input:
        response = "I'm here for you 🤗. Try listening to your favorite song or doodling something simple. Want to dance a bit?"
    elif "tired" in lower_input or "exhausted" in lower_input:
        response = "You might need some rest 🛌. Stretch for 2 minutes, drink water, and take a small break."
    elif "happy" in lower_input:
        response = "Yay! 😃 Celebrate by dancing, singing, or sketching a happy doodle today!"
    elif "bored" in lower_input:
        response = "Try a fun activity: dance, draw Doraemon, or organize your study desk with music on 🎶."
    elif "anxious" in lower_input or "nervous" in lower_input:
        response = "Take deep breaths 🧘‍♀️. Stretch your shoulders and journal your thoughts for clarity."
    elif "stomach" in lower_input or "headache" in lower_input or "pain" in lower_input:
        response = "Try drinking warm water and resting. If pain persists, please consult a doctor 🩺."
    elif "focus" in lower_input or "lazy" in lower_input:
        response = "Set a 15-min timer and start with a small task ⏱️. Reward yourself with a doodle or dance after!"
    else:
        response = "You can try dancing, singing, painting, exercising, or taking deep breaths today 🌻. Let me know how else I can help!"
    st.success(f"Doraemon says: {response}")

# To-Do List
st.markdown("## 📋 To-Do List")
tasks = st.session_state.get('tasks', [])
new_task = st.text_input("Add a new task to your list")
if new_task:
    tasks.append(new_task)
    st.session_state['tasks'] = tasks

completed = []
for idx, task in enumerate(tasks):
    if st.checkbox(task, key=idx):
        completed.append(task)
for task in completed:
    tasks.remove(task)
st.session_state['tasks'] = tasks

# Daily Quote
st.markdown("## ✨ Daily Quote")
quotes = ["Believe in yourself.", "Consistency creates results.", "Small steps build big dreams.", "Stay kind.", "You can do wonderful things."]
st.info(random.choice(quotes))

# Health Tip
st.markdown("## 🍎 Health Tip")
health_tips = ["Stay hydrated.", "Take breathing breaks.", "Eat fruits.", "Stretch shoulders.", "Walk for 10 min."]
st.info(random.choice(health_tips))

# Streak Tracker
st.markdown("## 🔥 Streak Tracker")
if 'streak' not in st.session_state:
    st.session_state['streak'] = 0
if st.button("✅ I completed today's tasks!"):
    st.session_state['streak'] += 1
    st.balloons()
    st.success(f"Great job! Streak: {st.session_state['streak']} days.")
else:
    st.info(f"Current streak: {st.session_state['streak']} days. Keep going!")

