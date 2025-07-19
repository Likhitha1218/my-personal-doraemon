import streamlit as st
import datetime
import random

# Page settings
st.set_page_config(page_title="My Personal Doraemon", page_icon="🐱", layout="centered")

# Pastel background styling using containers
st.markdown(
    """
    <style>
    .block-container {
        padding: 2rem;
        background-color: #fef6fb;
        border-radius: 20px;
    }
    h1, h2, h3 {
        font-family: Comic Sans MS, cursive;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Cartoon Images (stable Imgur links)
DORAEMON_URL = "https://i.imgur.com/bNxNqOd.png"
NOBITA_URL = "https://i.imgur.com/pKZtF7y.png"
SHIZUKA_URL = "https://i.imgur.com/1S5kAYt.png"
CARTOON_URLS = [
    "https://i.imgur.com/bNxNqOd.png",
    "https://i.imgur.com/pKZtF7y.png",
    "https://i.imgur.com/1S5kAYt.png",
    "https://i.imgur.com/FWZJtzu.png",
    "https://i.imgur.com/Opm9U8J.png"
]

# Header with Doraemon
col1, col2 = st.columns([1, 8])
with col1:
    st.image(DORAEMON_URL, width=80, use_container_width=False)
with col2:
    st.markdown("<h1>My Personal Doraemon</h1>", unsafe_allow_html=True)

# Date and Day with Nobita and Shizuka
today = datetime.datetime.now()
date_str = today.strftime("%d %B %Y")
day_str = today.strftime("%A")

col3, col4, col5, col6 = st.columns([1, 3, 1, 3])
with col3:
    st.image(NOBITA_URL, width=50, use_container_width=False)
with col4:
    st.markdown(f"### {date_str}")
with col5:
    st.image(SHIZUKA_URL, width=50, use_container_width=False)
with col6:
    st.markdown(f"### {day_str}")

# Daily Cartoon Doodle
today_index = today.timetuple().tm_yday % len(CARTOON_URLS)
st.image(CARTOON_URLS[today_index], caption="Today's Cartoon Doodle", use_container_width=True)

# Doraemon Prompt Box with suggestions
st.markdown("## 💬 Doraemon Prompt Box")
with st.form(key="prompt_form"):
    user_input = st.text_input("Tell Doraemon how you feel or what you need today:")
    submit = st.form_submit_button("Get Suggestion")

if submit and user_input:
    lower_input = user_input.lower()
    response = "✨ Doraemon says: "

    if any(word in lower_input for word in ["sad", "depressed", "upset", "cry"]):
        response += "I'm here for you 🤗. Try a light doodle, listen to your favorite song, or take a small walk."
    elif any(word in lower_input for word in ["tired", "exhausted", "sleepy"]):
        response += "You deserve rest 😴. Take a deep breath, stretch, or have a glass of water."
    elif "happy" in lower_input:
        response += "Yay! 😃 Celebrate your happiness by dancing or drawing something joyful."
    elif "bored" in lower_input:
        response += "Try dancing, singing, or doodling something fun 🎨 to refresh your mind."
    elif any(word in lower_input for word in ["anxious", "nervous", "worried"]):
        response += "Take slow breaths 🧘‍♀️. You can also try journaling your thoughts."
    elif any(word in lower_input for word in ["pain", "stomach", "headache"]):
        response += "Drink warm water, rest, and if it persists, please consult a doctor 🩺."
    elif any(word in lower_input for word in ["lazy", "focus", "can't study"]):
        response += "Set a 15-minute timer and start with a small task ⏱️. You can do it!"
    else:
        response += "You can try dancing, singing, painting, stretching, or journaling 🌻 to brighten your day."

    st.success(response)

# To-Do List with checkmarks
st.markdown("## 📋 To-Do List")
if 'tasks' not in st.session_state:
    st.session_state['tasks'] = []

new_task = st.text_input("Add a task:")
if st.button("Add Task") and new_task:
    st.session_state['tasks'].append(new_task)

for i, task in enumerate(st.session_state['tasks']):
    if st.checkbox(task, key=f"task_{i}"):
        st.session_state['tasks'].pop(i)
        st.experimental_rerun()

# Daily Quote
st.markdown("## ✨ Daily Quote")
quotes = [
    "Believe in yourself.",
    "Consistency creates results.",
    "Small steps build big dreams.",
    "Stay kind.",
    "You can do wonderful things."
]
st.info(random.choice(quotes))

# Health Tip
st.markdown("## 🍎 Health Tip")
health_tips = [
    "Stay hydrated.",
    "Take breathing breaks.",
    "Eat fruits.",
    "Stretch shoulders.",
    "Walk for 10 min."
]
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



