# Doraemon Aesthetic Productivity App with Stable Images for Streamlit Cloud

import streamlit as st
import datetime
import random

st.set_page_config(page_title="My Personal Doraemon", page_icon="🐱", layout="centered")

# Animated pastel background
animated_bg = """
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
"""
st.markdown(animated_bg, unsafe_allow_html=True)

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
    st.image(DORAEMON_URL, width=70)
with col2:
    st.markdown("<h1 style='font-family:Comic Sans MS;color:#2b2b2b;'>My Personal Doraemon</h1>", unsafe_allow_html=True)

# Date and day with Nobita and Shizuka
today = datetime.datetime.now()
date_str = today.strftime("%d %B %Y")
day_str = today.strftime("%A")
col3, col4, col5, col6 = st.columns([1, 3, 1, 3])
with col3:
    st.image(NOBITA_URL, width=50)
with col4:
    st.markdown(f"### {date_str}")
with col5:
    st.image(SHIZUKA_URL, width=50)
with col6:
    st.markdown(f"### {day_str}")

# Daily cartoon doodle
today_index = today.timetuple().tm_yday % len(CARTOON_URLS)
st.image(CARTOON_URLS[today_index], caption="Today's Cartoon Doodle", use_column_width=True)

# Prompt Box
st.markdown("## 💬 Prompt Box")
mood = st.text_input("How are you feeling today? Type 'exercise', 'dance', 'sing', 'paint' for suggestions:")
if mood:
    mood_lower = mood.lower()
    if "exercise" in mood_lower or "workout" in mood_lower or "fitness" in mood_lower:
        suggestions = ["Try 10 jumping jacks.", "Do a 1-minute wall sit.", "5 push-ups for energy.", "Stretch for 2 minutes.", "Deep breathing in a yoga pose."]
    elif "dance" in mood_lower:
        suggestions = ["Dance to your favorite song.", "Freestyle dance for 3 minutes.", "Groove lightly while studying.", "Silly dance to boost mood."]
    elif "sing" in mood_lower:
        suggestions = ["Sing your favorite song.", "Hum softly for relaxation.", "Sing to release stress.", "Record yourself singing."]
    elif "paint" in mood_lower or "draw" in mood_lower or "doodle" in mood_lower:
        suggestions = ["Doodle on a sticky note.", "Watercolor for 5 minutes.", "Draw stars or clouds.", "Sketch your mood as a cartoon."]
    else:
        suggestions = ["Dance for 5 min!", "Sing softly.", "Draw a doodle.", "Take a mindful walk.", "2-min breathing exercise.", "Write 3 gratitudes.", "Stretch for 5 min.", "Tidy your desk."]
    st.success(f"✨ Suggestion: {random.choice(suggestions)}")

# To-Do List
st.markdown("## 📋 To-Do List")
tasks = st.experimental_get_query_params().get("tasks", [])
new_task = st.text_input("Add a new task")
if new_task:
    tasks.append(new_task)
    st.experimental_set_query_params(tasks=tasks)
completed_tasks = []
for i, task in enumerate(tasks):
    if st.checkbox(task, key=i):
        completed_tasks.append(task)
tasks = [task for task in tasks if task not in completed_tasks]
st.experimental_set_query_params(tasks=tasks)

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
try:
    with open("streak.txt", "r") as f:
        streak = int(f.read())
except:
    streak = 0
if st.button("✅ I completed today's tasks!"):
    streak += 1
    with open("streak.txt", "w") as f:
        f.write(str(streak))
    st.balloons()
    st.success(f"Great job! Streak: {streak} days.")
else:
    st.info(f"Current streak: {streak} days. Keep going!")
