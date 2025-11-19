import google.generativeai as genai
import os
import tkinter as tk
from tkinter import scrolledtext, messagebox
from tkinter import *

# ---------------------------
# GOOGLE API KEY LOAD
# ---------------------------
api_key = os.getenv("GOOGLE_GENAI_API_KEY")

if not api_key:
    messagebox.showerror("API Key Error", "GOOGLE_GENAI_API_KEY not set in environment variables.")
    exit(1)

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")


# ---------------------------
# BACKEND FUNCTION
# ---------------------------
def generate_learning_path(profile):
    prompt = f"""
    You are an AI Learning Path Generator. Create a structured and detailed learning roadmap.
    User Profile:
    Skill Level: {profile['skill_level']}
    Career Goal: {profile['goal']}
    Weekly Study Time: {profile['time']}
    Topics of Interest: {profile['topics']}

    Provide:
    1. Step-by-step learning plan
    2. Weekly schedule
    3. Recommended resources
    4. Tools & projects for practice
    """
    response = model.generate_content(prompt)
    return response.text


# ---------------------------
# GUI ACTION FUNCTION
# ---------------------------
def on_submit():
    skill = skill_entry.get()
    goal = goal_entry.get()
    time = time_entry.get()
    topics = topics_entry.get()

    if skill == "" or goal == "" or time == "" or topics == "":
        messagebox.showwarning("Missing Data", "All fields must be filled.")
        return

    output_box.delete(1.0, END)
    output_box.insert(END, "Generating learning path...\nPlease wait...\n")

    try:
        profile = {
            "skill_level": skill,
            "goal": goal,
            "time": time,
            "topics": topics
        }

        result = generate_learning_path(profile)
        output_box.delete(1.0, END)
        output_box.insert(END, result)

    except Exception as e:
        output_box.delete(1.0, END)
        output_box.insert(END, "ERROR: Could not generate output.\n")
        output_box.insert(END, str(e))


# ---------------------------
# TKINTER GUI
# ---------------------------

root = Tk()
root.title("AI Learning Path Recommender")
root.geometry("850x600")
root.config(bg="#e3f2fd")  # Soft blue background

title_label = Label(root, text="AI Learning Path Recommender", font=("Arial", 20, "bold"), bg="#e3f2fd")
title_label.pack(pady=10)

# FRAME FOR INPUTS
frame = Frame(root, bg="#e3f2fd")
frame.pack(pady=10)

# Skill Level
Label(frame, text="Skill Level:", bg="#e3f2fd", font=("Arial", 12)).grid(row=0, column=0, sticky=W, pady=5)
skill_entry = Entry(frame, width=40)
skill_entry.grid(row=0, column=1, pady=5)

# Career Goal
Label(frame, text="Career Goal:", bg="#e3f2fd", font=("Arial", 12)).grid(row=1, column=0, sticky=W, pady=5)
goal_entry = Entry(frame, width=40)
goal_entry.grid(row=1, column=1, pady=5)

# Study Time
Label(frame, text="Study Time per Week (hours):", bg="#e3f2fd", font=("Arial", 12)).grid(row=2, column=0, sticky=W, pady=5)
time_entry = Entry(frame, width=40)
time_entry.grid(row=2, column=1, pady=5)

# Topics
Label(frame, text="Topics of Interest:", bg="#e3f2fd", font=("Arial", 12)).grid(row=3, column=0, sticky=W, pady=5)
topics_entry = Entry(frame, width=40)
topics_entry.grid(row=3, column=1, pady=5)

# Submit Button
submit_btn = Button(root, text="Generate Learning Path", command=on_submit, font=("Arial", 14), bg="#64b5f6", fg="black")
submit_btn.pack(pady=15)

# Output Box
output_box = scrolledtext.ScrolledText(root, width=100, height=20, font=("Courier", 10))
output_box.pack(pady=10)

root.mainloop()
