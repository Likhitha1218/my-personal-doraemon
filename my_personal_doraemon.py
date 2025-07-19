import streamlit as st
import datetime
import json
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

# -------------------- Google Calendar Setup --------------------
SCOPES = ['https://www.googleapis.com/auth/calendar.events']
calendar_id = 'primary'

def authenticate_gcal():
    creds = None
    if os.path.exists('token.pkl'):
        with open('token.pkl', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pkl', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def add_event_to_gcal(task):
    creds = authenticate_gcal()
    service = build('calendar', 'v3', credentials=creds)
    today_date = datetime.date.today()

    if "study" in task.lower() or "revise" in task.lower():
        color_id = "9"  # Blue
    elif "walk" in task.lower() or "stretch" in task.lower() or "health" in task.lower():
        color_id = "10"  # Green
    else:
        color_id = "5"   # Yellow

    event = {
        'summary': task,
        'start': {'dateTime': f"{today_date}T09:00:00", 'timeZone': 'Asia/Kolkata'},
        'end': {'dateTime': f"{today_date}T10:00:00", 'timeZone': 'Asia/Kolkata'},
        'colorId': color_id,
        'reminders': {
            'useDefault': False,
            'overrides': [{'method': 'popup', 'minutes': 10}]
        },
    }
    service.events().insert(calendarId=calendar_id, body=event).execute()

# -------------------- Streak Tracking --------------------
streak_file = 'doraemon_streak.json'

def load_streak():
    if os.path.exists(streak_file):
        with open(streak_file, 'r') as f:
            return json.load(f)
    else:
        return {"last_date": "", "streak": 0}

def save_streak(data):
    with open(streak_file, 'w') as f:
        json.dump(data, f, indent=4)

today_date = datetime.date.today()
streak_data = load_streak()

if streak_data["last_date"] != str(today_date):
    last_date_obj = datetime.datetime.strptime(streak_data["last_date"], "%Y-%m-%d").date() if streak_data["last_date"] else None
    if last_date_obj and (today_date - last_date_obj).days == 1:
        streak_data["streak"] += 1
    else:
        streak_data["streak"] = 1
    streak_data["last_date"] = str(today_date)
    save_streak(streak_data)

# -------------------- Aesthetic --------------------
st.set_page_config(page_title="My Personal Doraemon", layout="centered")

st.markdown("""
<style>
body { background-color: #fceff9; font-family: 'Comic Sans MS', cursive; }
h1, h2, h3 { color: #ff6f91; }
.stButton>button {
    background-color: #ff6f91; color: white; border-radius: 15px;
    padding: 0.5em 1em; font-size: 1em; font-weight: bold;
}
.stButton>button:hover { background-color: #ff8ba7; }
</style>
""", unsafe_allow_html=True)

# -------------------- Header --------------------
st.markdown(f"<h1>💙 My Personal Doraemon</h1>", unsafe_allow_html=True)
st.markdown(f"<h3>🔥 Current Streak: {streak_data['streak']} days</h3>", unsafe_allow_html=True)

# -------------------- To-Do List --------------------
st.markdown("---")
st.markdown("<h2>📝 Today's To-Do List</h2>", unsafe_allow_html=True)

todo_file = "doraemon_todo.json"

def load_todos():
    if os.path.exists(todo_file):
        with open(todo_file, "r") as f:
            return json.load(f)
    else:
        return {}

def save_todos(todos):
    with open(todo_file, "w") as f:
        json.dump(todos, f, indent=4)

todos = load_todos()
today_str = str(today_date)
if today_str not in todos:
    todos[today_str] = [
        {"task": "📖 Study 2 hours (Core Subject/IAS GS)", "done": False},
        {"task": "🧘‍♀️ 10-min morning stretching", "done": False},
        {"task": "🚶‍♀️ 15-min evening walk", "done": False},
        {"task": "📚 Revise yesterday's notes", "done": False},
        {"task": "🧑‍🍳 Help family with one chore", "done": False},
    ]

for idx, item in enumerate(todos[today_str]):
    checked = st.checkbox(item["task"], value=item["done"], key=f"todo_{idx}")
    if checked and not item["done"]:
        add_event_to_gcal(item["task"])
    todos[today_str][idx]["done"] = checked

new_task = st.text_input("Add a new task:")
if st.button("➕ Add Task"):
    if new_task.strip() != "":
        todos[today_str].append({"task": new_task, "done": False})
        save_todos(todos)
        add_event_to_gcal(new_task)
        st.experimental_rerun()

save_todos(todos)

# -------------------- Quote --------------------
st.markdown("---")
st.markdown("<h2>💡 Doraemon's Quote of the Day</h2>", unsafe_allow_html=True)
quotes = [
    "Believe in yourself, even if no one else does.",
    "Consistency beats motivation every time.",
    "Take small steps, and they will lead to big changes.",
    "Rest if you must, but don’t quit.",
    "Your hard work will pay off, keep going!"
]
quote_today = quotes[today_date.timetuple().tm_yday % len(quotes)]
st.success(f"✨ {quote_today}")

# -------------------- Health Tip --------------------
st.markdown("---")
st.markdown("<h2>🍎 Doraemon's Health Tip of the Day</h2>", unsafe_allow_html=True)
health_tips = [
    "Drink 2-3 litres of water today.",
    "Take deep belly breaths to reduce stress.",
    "Eat at least one fruit today.",
    "Avoid screens 30 mins before bed for better sleep.",
    "Do some light stretches if you feel stiff while studying."
]
health_tip_today = health_tips[today_date.timetuple().tm_yday % len(health_tips)]
st.info(f"💡 {health_tip_today}")
