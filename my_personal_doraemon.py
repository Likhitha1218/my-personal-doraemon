import streamlit as st
import datetime
import random

# Page configuration
st.set_page_config(page_title="My Personal Doraemon", page_icon="🐱", layout="centered")

# Simple light pastel background simulation
st.markdown(
    '''
    <style>
    .stApp {
        background-color: #FFF8F0;
    }
    </style>
    ''',
    unsafe_allow_html=True
)

# Stable cartoon images (using Imgur)
DORAEMON_URL = "https://i.imgur.com/bNxNqOd.png"
NOBITA_URL = "https://i.imgur.com/pKZtF7y.png"
SHIZUKA_URL = "https://i.imgur.com/1S5kAYt.png"
CARTOON_URLS = [
    "https://i.imgur.com/bNxNqOd.png",
    "https://i.imgur.com/pKZtF7y.png",
    "https://i.imgur.com/1S5kAYt.png"
]

# Header with Doraemon image
st.image(DORAEMON_URL, width=120)
st.markdown("<h1 style='text-align: center; font-family: Comic Sans MS;'>My Personal Doraemon</h1>", unsafe_allow_html=True)

# Date and day with Nobita and Shizuka
today = datetime.datetime.now()
date_str = today.strftime("%d %B %Y")
day_str = today.strftime("%A")
st.markdown(f"### 📅 {date_str} &nbsp;&nbsp;&nbsp; 🗓️ {day_str}")

cols = st.columns([1, 6, 1])
with cols[0]:
    st.image(NOBITA_URL, width=60)
with cols[2]:
    st.image(SHIZUKA_URL, width=60)

# Daily cartoon doodle
today_index = today.timetuple().tm_yday % len(CARTOON_URLS)
st.image(CARTOON_URLS[today_index], caption="Today's Cartoon Doodle")

# Conversational Doraemon Prompt Box with memory
st.markdown("## 💬 Doraemon Chat")
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

user_input = st.text_input("👧 Tell Doraemon how you feel or what you need today:")

if st.button("💌 Get Doraemon's Suggestion"):
    lower_input = user_input.lower()
    response = "✨ Doraemon says: "

    if any(word in lower_input for word in ["sad", "cry", "depressed"]):
        response += "I'm here for you 🤗. Let’s take a small walk or doodle something simple."
    elif any(word in lower_input for word in ["tired", "sleepy", "exhausted"]):
        response += "Rest is important 😴. Try stretching and hydrate well."
    elif "happy" in lower_input:
        response += "Yay! 😃 How about dancing or drawing a Doraemon today?"
    elif "bored" in lower_input:
        response += "Try dancing, singing, or painting something new 🎨."
    elif any(word in lower_input for word in ["anxious", "nervous", "stress"]):
        response += "Take a deep breath 🧘‍♀️. Let’s journal a gratitude list together."
    elif any(word in lower_input for word in ["pain", "stomach", "headache"]):
        response += "Please drink warm water and rest. If it continues, consult a doctor 🩺."
    elif any(word in lower_input for word in ["lazy", "focus", "study"]):
        response += "Start with a 15-min focus timer ⏱️ and reward yourself with a break after!"
    else:
        response += "How about dancing, singing, painting, or going for a short walk today? 🌻"

    st.session_state.chat_history.append(("👧 You: " + user_input, response))

for user_text, bot_text in reversed(st.session_state.chat_history):
    st.info(f"{user_text}\n{bot_text}")

# To-Do List with checkmarks
st.markdown("## ✅ To-Do List")
if 'tasks' not in st.session_state:
    st.session_state['tasks'] = []

new_task = st.text_input("Add a task:")
if st.button("➕ Add Task") and new_task:
    st.session_state['tasks'].append(new_task)

for i, task in enumerate(st.session_state['tasks']):
    if st.checkbox(task, key=f"task_{i}"):
        st.session_state['tasks'].pop(i)
        st.experimental_rerun()

# Daily Quote
st.markdown("## ✨ Daily Quote")
quotes = [
    "Believe in yourself.",
    "Small steps build big dreams.",
    "Stay kind.",
    "You can do wonderful things.",
    "Consistency creates results."
]
st.success(random.choice(quotes))

# Health Tip
st.markdown("## 🍎 Health Tip")
health_tips = [
    "Drink plenty of water 💧.",
    "Take deep breathing breaks 🌬️.",
    "Eat fruits 🍎.",
    "Stretch your shoulders 🙆‍♀️.",
    "Take a 10-min walk 🚶."
]
st.success(random.choice(health_tips))

# Streak Tracker
st.markdown("## 🔥 Streak Tracker")
if 'streak' not in st.session_state:
    st.session_state['streak'] = 0

if st.button("✅ I completed today's goals!"):
    st.session_state['streak'] += 1
    st.balloons()
    st.success(f"Great job! You have a {st.session_state['streak']} day streak 🎉.")

else:
    st.info(f"Your current streak: {st.session_state['streak']} days. Keep it up!")




