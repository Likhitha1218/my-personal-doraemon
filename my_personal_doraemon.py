import streamlit as st
import datetime
import random

# Page Configuration
st.set_page_config(page_title="My Personal Doraemon", page_icon="🐱", layout="centered")

# Pastel background, Fredoka One font, clear text color
st.markdown('''
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka+One&display=swap');
    .stApp {
        background-image: url("https://raw.githubusercontent.com/abhishekkrthakur/ImagesForProjects/main/pastel_doodle.png");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        color: #222;
        font-family: 'Fredoka One', cursive;
    }
    h1, h2, h3, h4, h5, h6, p, div, span, input, button {
        color: #222 !important;
        font-family: 'Fredoka One', cursive;
    }
    .block {
        background-color: #FFFFFFDD;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .stTextInput>div>div>input {
        background-color: #FFEFEF;
        color: #222;
    }
    .stButton>button {
        background-color: #FFD6E8;
        color: #222;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5em 1em;
    }
    </style>
''', unsafe_allow_html=True)

# App Title
st.markdown("<h1 style='text-align: center;'>My Personal Doraemon 🩵</h1>", unsafe_allow_html=True)

# Date and Day
today = datetime.datetime.now()
date_str = today.strftime("%d %B %Y")
day_str = today.strftime("%A")
st.markdown(f"<h3 style='text-align:center;'>{date_str} | {day_str}</h3>", unsafe_allow_html=True)

# Streak Tracker
if 'streak' not in st.session_state:
    st.session_state['streak'] = 0
if 'last_checked' not in st.session_state:
    st.session_state['last_checked'] = today.date()

if st.session_state['last_checked'] != today.date():
    st.session_state['streak'] += 1
    st.session_state['last_checked'] = today.date()

st.markdown("<div class='block'>", unsafe_allow_html=True)
st.markdown(f"## 🔥 Streak: {st.session_state['streak']} days of consistency!")
st.markdown("</div>", unsafe_allow_html=True)

# To-Do List with default tasks
st.markdown("<div class='block'>", unsafe_allow_html=True)
st.markdown("## ✅ To-Do List")

if 'tasks' not in st.session_state:
    st.session_state['tasks'] = [
        "🌸 Read for 30 minutes",
        "🚶‍♀️ Take a 10-minute walk",
        "🤖 Revise one AI/ML topic",
        "💧 Drink water",
        "📝 Journal for 5 minutes"
    ]

new_task = st.text_input("Add a new task:")
if st.button("Add Task") and new_task.strip() != "":
    st.session_state['tasks'].append(new_task.strip())

completed_tasks = []

for i, task in enumerate(st.session_state['tasks']):
    if st.checkbox(task, key=f"task_{i}"):
        completed_tasks.append(i)

# Remove completed tasks after loop
if completed_tasks:
    for index in sorted(completed_tasks, reverse=True):
        st.session_state['tasks'].pop(index)
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

# Daily Quote
st.markdown("<div class='block'>", unsafe_allow_html=True)
st.markdown("## ✨ Daily Quote")
quotes = [
    "🌼 You are capable of amazing things!",
    "💫 Take a deep breath, you are doing well.",
    "🌻 Stay consistent, and you will see progress.",
    "😊 Smile, it suits you!",
    "🌈 Today is a new opportunity to grow."
]
st.success(random.choice(quotes))
st.markdown("</div>", unsafe_allow_html=True)

# Health Tip
st.markdown("<div class='block'>", unsafe_allow_html=True)
st.markdown("## 🍎 Health Tip")
health_tips = [
    "💧 Drink a glass of water now",
    "🧘‍♀️ Stretch your body for 5 minutes",
    "🍎 Eat a fruit today",
    "🌬️ Take deep breaths for a minute",
    "🚶‍♀️ Go for a short walk"
]
st.success(random.choice(health_tips))
st.markdown("</div>", unsafe_allow_html=True)

# Prompt Box
st.markdown("<div class='block'>", unsafe_allow_html=True)
st.markdown("## 💬 Ask Doraemon")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

user_input = st.text_input("Tell Doraemon how you feel or what you need today 💖")

if st.button("Ask Doraemon"):
    user_text = user_input.lower()
    response = "✨ Doraemon says: "

    if "sad" in user_text or "depress" in user_text:
        response += "It's okay to feel this way 🌸. Try painting, doodling, or going for a walk."
    elif "happy" in user_text:
        response += "That's wonderful! Celebrate with dance, music, or art 🌈."
    elif "bored" in user_text:
        response += "How about singing, painting, or trying a new hobby today 🎨?"
    elif "tired" in user_text:
        response += "Take a short nap or stretch gently 🧘‍♀️."
    elif "focus" in user_text or "study" in user_text:
        response += "Use Pomodoro: 25 min focus, 5 min break 📚."
    elif "pain" in user_text or "headache" in user_text:
        response += "Drink water, rest, and take deep breaths 💧."
    elif "exercise" in user_text or "workout" in user_text:
        response += "Try gentle stretches or a short dance session 💃."
    else:
        response += "You can dance, paint, journal, or take a walk to refresh today! 💫"

    st.session_state['chat_history'].append((f"👧 You: {user_input}", response))

for user, reply in reversed(st.session_state['chat_history']):
    st.info(f"{user}\n{reply}")

st.markdown("</div>", unsafe_allow_html=True)

