import streamlit as st
import datetime
import random

# Page config
st.set_page_config(page_title="My Personal Doraemon", page_icon="🐱", layout="centered")

# Inject pastel background with clear dark text
st.markdown(
    '''
    <style>
    .stApp {
        background-color: #FFF8F0;
        color: #333333;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    h1, h2, h3, h4, h5, h6, p {
        color: #333333;
    }
    .block {
        background-color: #FFFFFF;
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }
    </style>
    ''',
    unsafe_allow_html=True
)

# Cartoon image URLs
DORAEMON_URL = "https://i.imgur.com/bNxNqOd.png"
NOBITA_URL = "https://i.imgur.com/pKZtF7y.png"
SHIZUKA_URL = "https://i.imgur.com/1S5kAYt.png"
CARTOONS = [
    "https://i.imgur.com/bNxNqOd.png",
    "https://i.imgur.com/pKZtF7y.png",
    "https://i.imgur.com/1S5kAYt.png"
]

# Header
st.image(DORAEMON_URL, width=120)
st.markdown("<h1 style='text-align: center;'>My Personal Doraemon</h1>", unsafe_allow_html=True)

# Date & Day with Nobita & Shizuka
today = datetime.datetime.now()
date_str = today.strftime("%d %B %Y")
day_str = today.strftime("%A")
cols = st.columns([1, 6, 1])
with cols[0]:
    st.image(NOBITA_URL, width=60)
with cols[1]:
    st.markdown(f"<h3 style='text-align:center;'>{date_str} | {day_str}</h3>", unsafe_allow_html=True)
with cols[2]:
    st.image(SHIZUKA_URL, width=60)

# Daily cartoon doodle
st.markdown("<div class='block'>", unsafe_allow_html=True)
today_index = today.timetuple().tm_yday % len(CARTOONS)
st.image(CARTOONS[today_index], caption="Today's Cartoon Doodle", use_column_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# To-Do List Section
st.markdown("<div class='block'>", unsafe_allow_html=True)
st.markdown("## ✅ To-Do List")
if 'tasks' not in st.session_state:
    st.session_state['tasks'] = []

new_task = st.text_input("Add a new task here:")
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

# Conversational Prompt Box
st.markdown("<div class='block'>", unsafe_allow_html=True)
st.markdown("## 💬 Doraemon Chat")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

user_prompt = st.text_input("👧 Tell Doraemon how you feel or what you need:")

if st.button("Get Doraemon's Advice"):
    lower_prompt = user_prompt.lower()
    response = "✨ Doraemon says: "

    # Advanced smart logic for human + study + health needs
    if "sad" in lower_prompt or "depress" in lower_prompt:
        response += "It's okay to feel sad. Let's paint or take a slow walk to clear your mind."
    elif "happy" in lower_prompt:
        response += "That's awesome! Celebrate by dancing or doing something creative!"
    elif "bored" in lower_prompt:
        response += "Try sketching Doraemon or singing your favorite song!"
    elif "tired" in lower_prompt or "sleepy" in lower_prompt:
        response += "Take a 15-minute power nap and hydrate yourself well."
    elif "focus" in lower_prompt or "study" in lower_prompt:
        response += "Use the Pomodoro technique: 25 min focused study, 5 min break!"
    elif "pain" in lower_prompt or "headache" in lower_prompt or "stomach" in lower_prompt:
        response += "Take deep breaths, drink warm water, and rest. If it continues, please consult a doctor."
    elif "exercise" in lower_prompt or "workout" in lower_prompt:
        response += "How about a 10-minute dance or stretching session now?"
    else:
        response += "How about dancing, painting, singing, or reading something you love today?"

    st.session_state.chat_history.append(("👧 You: " + user_prompt, response))

# Display conversation history
for user_text, bot_reply in reversed(st.session_state['chat_history']):
    st.info(f"{user_text}\n{bot_reply}")
")

st.markdown("</div>", unsafe_allow_html=True)
