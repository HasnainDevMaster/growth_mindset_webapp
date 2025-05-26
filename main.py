import streamlit as st
import pandas as pd
import uuid
import datetime
import json
from pathlib import Path

# ------------------- File Setup -------------------
DATA_FILE = Path("growth_data.json")
if not DATA_FILE.exists():
    DATA_FILE.write_text(json.dumps({"entries": [], "streak": 0, "last_entry_date": ""}))

# ------------------- Load Data -------------------
def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ------------------- App Config -------------------
st.set_page_config(page_title="Growth Mindset Tracker", layout="centered")
st.title("🌱 Growth Mindset Tracker")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Daily Reflection", "Set a Goal", "My Progress", "Growth Wall"])

# ------------------- Daily Reflection -------------------
if page == "Daily Reflection":
    st.header("🧠 Daily Reflection")
    today = datetime.date.today().strftime("%Y-%m-%d")
    challenge = st.text_area("What challenge did you face today?")
    learning = st.text_area("What did you learn from it?")

    if st.button("Save Reflection"):
        if challenge and learning:
            data = load_data()
            last_date = data.get("last_entry_date", "")
            streak = data.get("streak", 0)

            if last_date:
                last_date_obj = datetime.datetime.strptime(last_date, "%Y-%m-%d").date()
                if (datetime.date.today() - last_date_obj).days == 1:
                    streak += 1
                elif (datetime.date.today() - last_date_obj).days > 1:
                    streak = 1
            else:
                streak = 1

            entry = {
                "id": str(uuid.uuid4()),
                "date": today,
                "challenge": challenge,
                "learning": learning
            }
            data["entries"].append(entry)
            data["streak"] = streak
            data["last_entry_date"] = today
            save_data(data)
            st.success(f"Reflection saved! 🔥 Current streak: {streak} days")
        else:
            st.warning("Please fill out both fields.")

# ------------------- Set a Goal -------------------
elif page == "Set a Goal":
    st.header("🎯 Set a Learning Goal")
    goal_title = st.text_input("Goal Title")
    goal_desc = st.text_area("Goal Description")
    deadline = st.date_input("Deadline")

    if st.button("Add Goal"):
        if goal_title and goal_desc:
            data = load_data()
            goal = {
                "id": str(uuid.uuid4()),
                "date": datetime.date.today().strftime("%Y-%m-%d"),
                "goal": goal_title,
                "description": goal_desc,
                "deadline": str(deadline)
            }
            data.setdefault("goals", []).append(goal)
            save_data(data)
            st.success("Goal added!")
        else:
            st.warning("Please provide both goal title and description.")

# ------------------- My Progress -------------------
elif page == "My Progress":
    st.header("📈 My Growth Progress")
    data = load_data()
    entries = data.get("entries", [])
    goals = data.get("goals", [])
    streak = data.get("streak", 0)

    # Show emoji badge based on streak
    st.subheader("🔥 Current Streak")
    if streak >= 10:
        st.markdown(f"🥇 **Streak: {streak} days - Mindset Master!**")
    elif streak >= 5:
        st.markdown(f"🏅 **Streak: {streak} days - Growth Warrior!**")
    elif streak >= 3:
        st.markdown(f"💪 **Streak: {streak} days - Learner in Action!**")
    elif streak > 0:
        st.markdown(f"🌟 **Streak: {streak} day(s) - Keep it up!**")
    else:
        st.info("Start journaling to build your streak!")

    st.subheader("Reflections Over Time")
    if entries:
        df = pd.DataFrame(entries)
        st.line_chart(df["date"].value_counts().sort_index())
    else:
        st.info("No reflections yet.")

    st.subheader("Goals")
    if goals:
        for g in goals:
            st.markdown(f"**{g['goal']}** - Due: {g['deadline']}\n> {g['description']}")
    else:
        st.info("No goals added yet.")

# ------------------- Growth Wall -------------------
elif page == "Growth Wall":
    st.header("🧱 Growth Wall")
    data = load_data()
    entries = data.get("entries", [])
    goals = data.get("goals", [])

    if entries:
        st.subheader("Recent Reflections")
        for entry in reversed(entries[-10:]):
            st.markdown(f"**📅 {entry['date']}**")
            st.markdown(f"**Challenge:** {entry['challenge']}")
            st.markdown(f"**Learning:** {entry['learning']}")
            st.markdown("---")
    else:
        st.info("No reflections yet.")

    if goals:
        st.subheader("Goals")
        for goal in goals:
            st.markdown(f"**🎯 {goal['goal']}** - Due: {goal['deadline']}")
            st.markdown(f"> {goal['description']}")
            st.markdown("---")
    else:
        st.info("No goals added yet.")
