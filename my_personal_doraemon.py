
import streamlit as st
import datetime
import random

# Page Configuration
st.set_page_config(page_title="My Personal Doraemon", page_icon="🐱", layout="centered")

# Custom CSS for pastel background, cartoonish fonts, and button styling
st.markdown('''
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@400;700&display=swap');
    .stApp {
        background-color: #FFF7F0;
        color: #333;
        font-family: 'Comic Neue', cursive;
    }
    .block {
        background-color: #FFFFFFCC;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .stTextInput>div>div>input {
        background-color: #FFF0F5;
        color: #222;
    }
    .stButton>button {
        background-color: #AEDFF7;
        color: #222;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5em 1em;
    }
    </style>
''', unsafe_allow_html=True)

# App Title
st.markdown("<h1 style='text-align: center;'>My Personal Doraemon</h1>", unsafe_allow_html=True)

# Display Current Date and Day
today = datetime.datetime.now()
date_str = today.strftime("%d %B %Y")
day_str = today.strftime("%A")
st.markdown(f"<h3 style='text-align:center;'>{date_str} | {day_str}</h3>", unsafe_allow_html=True)

# Display Dynamic Pastel Doodle Image
st.markdown("<div class='block'>", unsafe_allow_html=True)
doodle_url = f"https://source.unsplash.com/800x400/?pastel,doodle&sig={today.timetuple().tm_yday}"
st.image(doodle_url, caption="✨ Today's Pastel Doodle", use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# Streak Tracking
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
        "Read for 30 minutes 📚",
        "Take a 10-minute walk 🚶‍♀️",
        "Revise one AI/ML topic 🤖",
        "Drink water 💧",
        "Journal for 5 minutes 📝"
    ]

new_task = st.text_input("Add a new task:")
if st.button("Add Task") and new_task.strip() != "":
    st.session_state['tasks'].append(new_task.strip())

for i, task in enumerate(st.session_state['tasks']):
    if st.checkbox(task, key=f"task_{i}"):
        st.session_state['tasks'].pop(i)
        st.experimental_rerun()
st.markdown("</div>", unsafe_allow_html=True)

# Daily Quote Section
st.markdown("<div class='block'>", unsafe_allow_html=True)
st.markdown("## ✨ Daily Quote")
quotes = [
    "You are capable of amazing things!",
    "Take a deep breath, you are doing well.",
    "Stay consistent, and you will see progress.",
    "Smile, it suits you!",
    "Today is a new opportunity to grow."
]
st.success(random.choice(quotes))
st.markdown("</div>", unsafe_allow_html=True)

# Health Tip Section
st.markdown("<div class='block'>", unsafe_allow_html=True)
st.markdown("## 🍎 Health Tip")
health_tips = [
    "Drink a glass of water now 💧",
    "Stretch your body for 5 minutes 🧘‍♀️",
    "Eat a fruit today 🍎",
    "Take deep breaths for a minute 🌬️",
    "Go for a short walk 🚶‍♀️"
]
st.success(random.choice(health_tips))
st.markdown("</div>", unsafe_allow_html=True)

# Prompt Box for ChatGPT-like suggestions
st.markdown("<div class='block'>", unsafe_allow_html=True)
st.markdown("## 💬 Doraemon Chat")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

user_input = st.text_input("How are you feeling or what do you need today?")

if st.button("Ask Doraemon"):
    lower_input = user_input.lower()
    response = "✨ Doraemon says: "

    if "sad" in lower_input or "depress" in lower_input:
        response += "It's okay to feel this way. Try painting, doodling, or going for a short walk."
    elif "happy" in lower_input:
        response += "That's great! Celebrate with dance, music, or a creative hobby."
    elif "bored" in lower_input:
        response += "How about sketching, singing, or exploring a new hobby today?"
    elif "tired" in lower_input:
        response += "Take a 15-minute nap or relax with deep breaths."
    elif "focus" in lower_input or "study" in lower_input:
        response += "Try the Pomodoro method: 25 min focus, 5 min break."
    elif "pain" in lower_input or "headache" in lower_input:
        response += "Drink water, take deep breaths, and rest. If it persists, see a doctor."
    elif "exercise" in lower_input or "workout" in lower_input:
        response += "Try a 10-minute dance or a light stretch session!"
    else:
        response += "Dance, paint, read, or take a walk to refresh yourself today!"

    st.session_state.chat_history.append(("👧 You: " + user_input, response))

for user_text, bot_reply in reversed(st.session_state['chat_history']):
    st.info(f"{user_text}\n{bot_reply}")

st.markdown("</div>", unsafe_allow_html=True)

