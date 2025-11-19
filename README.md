# Learning-Path-Recommender
📘 Learning Path Recommender using Python & Google Generative AI

An AI-powered Learning Path Recommendation System that dynamically generates personalized learning roadmaps based on user input such as skill level, career goals, available time, and learning interests.

This project integrates the Google Generative AI (Gemini) API to produce high-quality personalized learning pathways using prompt engineering.

🚀 Features

✔ Google Generative AI (Gemini) integration

✔ Personalized learning recommendations

✔ Structured learning path with topics, sequence & estimated effort

✔ Python-based console interface (beginner-friendly)

✔ Clean architecture & modular code

✔ Fully documented project with diagrams & screenshots

✔ Ready for academic submission & portfolio use

📂 Project Structure
Learning-Path-Recommender/
│
├── learning_path_recommender.py
├── README.md
├── requirements.txt
└── /screenshots
      └── architecture.png

🧠 System Architecture
          ┌────────────────────────┐
          │   User Input Layer     │
          │(Skill, Goals, Time etc.)│
          └───────────┬────────────┘
                      │
                      ▼
          ┌────────────────────────┐
          │  Data Preprocessing    │
          │ (Formatting Prompt)    │
          └───────────┬────────────┘
                      │
                      ▼
          ┌────────────────────────┐
          │ Google Gemini API Call │
          │ (LLM Inference Engine) │
          └───────────┬────────────┘
                      │
                      ▼
          ┌────────────────────────┐
          │ AI-Generated Learning  │
          │   Path Recommendation  │
          └───────────┬────────────┘
                      │
                      ▼
          ┌────────────────────────┐
          │  Final Output to User  │
          └────────────────────────┘

🛠 Technologies Used

Python 3.8+

Google Generative AI (Gemini 1.5 Flash)

Prompt Engineering

VS Code

API Integration

Markdown Documentation

Diagram Generation

📦 Installation & Setup
1. Clone the repository
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

2. Install required libraries
pip install google-generativeai python-dotenv

3. Add your Google API key

Create a file .env in your project folder:

GOOGLE_GENAI_API_KEY=YOUR_API_KEY_HERE

4. Run the program
python learning_path_recommender.py

💻 Usage

When you run the program, it will ask:

Enter your current skill level (Beginner / Intermediate / Advanced):
Enter your career goal:
Enter weekly study time (in hours):
Enter topics you want to learn (comma-separated):


Then the AI generates a personalized learning plan.

📝 Sample Output
========================================
PERSONALIZED LEARNING PATH
========================================

Skill Level: Beginner
Career Goal: Become a Data Analyst
Weekly Study Time: 7 hours

Recommended Learning Path:
1. Python Basics (Week 1–2)
2. Data Analysis with Pandas (Week 3–4)
3. SQL for Data Analysis (Week 5)
4. Data Visualization (Week 6)
5. Mini Projects (Week 7)

Tools & Courses Suggested:
- Kaggle
- DataCamp
- FreeCodeCamp

Good luck on your learning journey!

📜 Code (Main Script)

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


🧾 References

Google Generative AI Documentation

Python Official Docs

MDN Web Docs

Coursera ML Courses

Kaggle Learn

YouTube (Tech With Tim, CodeWithHarry, Patrick Loeber)

📬 Connect With Me

Kushal Singh
Feel free to reach out or collaborate.
Contact Information:
Instagram- @kush__singh27
