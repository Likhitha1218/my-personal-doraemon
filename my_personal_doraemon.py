import streamlit as st
import datetime
import random

st.set_page_config(page_title="My Personal Doraemon", page_icon="🐱", layout="centered")

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

cartoon_urls = [
    "https://i.imgur.com/lr7xARU.png",
    "https://i.imgur.com/fnKqQ0p.png",
    "https://i.imgur.com/1YcKcVW.png",
    "https://i.imgur.com/EK1zMLP.png",
    "https://i.imgur.com/CODQMMQ.png",
    "https://i.imgur.com/qXANHfT.png",
    "https://i.imgur.com/OPOxDsA.png",
    "https://i.imgur.com/ZqPVn2Q.png",
    "https://i.imgur.com/mQOSyDD.png",
    "https://i.imgur.com/F5OZn5u.png"
]
today_index = datetime.datetime.now().timetuple().tm_yday % len(cartoon_urls)
today_cartoon = cartoon_urls[today_index]

doraemon_logo = "https://i.imgur.com/1YcKcVW.png"
col1, col2 = st.columns([1, 8])
with col1:
    st.image(doraemon_logo, width=70)
with col2:
    st.markdown("<h1 style='font-family:Comic Sans MS;color:#2b2b2b;'>My Personal Doraemon</h1>", unsafe_allow_html=True)

today = datetime.datetime.now()
date_str = today.strftime("%d %B %Y")
day_str = today.strftime("%A")
nobita_img = "https://i.imgur.com/W8yWxJd.png"
shizuka_img = "https://i.imgur.com/n4v4DdF.png"
col3, col4, col5, col6 = st.columns([1, 3, 1, 3])
with col3:
    st.image(nobita_img, width=40)
with col4:
    st.markdown(f"### {date_str}")
with col5:
    st.image(shizuka_img, width=40)
with col6:
    st.markdown(f"### {day_str}")

st.image(today_cartoon, caption="Today's Cartoon", use_column_width=True)

st.markdown("## 💬 Prompt Box")
mood = st.text_input("How are you feeling today? Type 'exercise', 'dance', 'sing', or 'paint' for suggestions:")
if mood:
    mood_lower = mood.lower()
    if "exercise" in mood_lower or "workout" in mood_lower or "fitness" in mood_lower:
        exercise_suggestions = [
            "Try 10 jumping jacks!",
            "Do a quick 1-minute wall sit.",
            "Do 5 push-ups to energize.",
            "Stretch for 2 minutes.",
            "Do 1-minute deep breathing in a yoga pose."
        ]
        suggestion = random.choice(exercise_suggestions)
    elif "dance" in mood_lower:
        dance_suggestions = [
            "Dance to your favorite song for 3 minutes!",
            "Try a freestyle dance break.",
            "Play a song and groove lightly while studying.",
            "Do a silly dance to boost your mood.",
            "Record yourself dancing for fun!"
        ]
        suggestion = random.choice(dance_suggestions)
    elif "sing" in mood_lower:
        sing_suggestions = [
            "Sing your favorite song for 2 minutes.",
            "Try humming to relax your mind.",
            "Sing loudly to release stress.",
            "Record yourself singing for fun!",
            "Sing along with your playlist."
        ]
        suggestion = random.choice(sing_suggestions)
    elif "paint" in mood_lower or "draw" in mood_lower or "doodle" in mood_lower:
        art_suggestions = [
            "Draw a small doodle on a sticky note.",
            "Try watercolor painting for 5 minutes.",
            "Doodle clouds or stars in your notebook.",
            "Draw your mood as a cartoon.",
            "Color a small mandala page."
        ]
        suggestion = random.choice(art_suggestions)
    else:
        general_suggestions = [
            "Take a 5-minute dance break!",
            "Sing your favorite song softly.",
            "Draw a small doodle to refresh your mind.",
            "Take a short mindful walk.",
            "Do a 2-minute breathing exercise.",
            "Write down 3 things you are grateful for.",
            "Stretch for 5 minutes.",
            "Tidy your desk quickly."
        ]
        suggestion = random.choice(general_suggestions)
    st.success(f"✨ Suggestion: {suggestion}")

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

st.markdown("## ✨ Daily Quote")
quotes = [
    "Believe in yourself and all that you are.",
    "Consistency creates results.",
    "Take small steps daily to build big dreams.",
    "Stay kind to yourself and others.",
    "You are capable of wonderful things."
]
st.info(random.choice(quotes))

st.markdown("## 🍎 Health Tip")
health_tips = [
    "Stay hydrated today.",
    "Take mindful breathing breaks.",
    "Eat a healthy fruit or snack.",
    "Stretch your back and shoulders.",
    "Take a 10-minute walk if possible."
]
st.info(random.choice(health_tips))

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
    st.success(f"Great job! Your current streak is {streak} days.")
else:
    st.info(f"Your current streak is {streak} days. Keep it up!")
