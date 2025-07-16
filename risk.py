import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont

def calculate_risk():
    """Calculate the risk level based on the user's responses."""
    score = 0

    # Get the responses from the options
    for var in question_vars:
        score += var.get()

    # Determine the risk level
    if score <= 5:
        risk_level = "Low Risk"
        advice = "You prefer stable investments with lower risks and returns."
    elif 6 <= score <= 10:
        risk_level = "Moderate Risk"
        advice = "You are open to some risk for higher returns but value a balanced approach."
    else:
        risk_level = "High Risk"
        advice = "You are willing to take higher risks for potentially higher returns."

    # Display the risk level
    messagebox.showinfo("Risk Level", f"Your Risk Level: {risk_level}\n\nAdvice: {advice}")

def next_question():
    """Move to the next question."""
    global current_question
    if current_question < len(questions) - 1:
        current_question += 1
        display_question(current_question)

def previous_question():
    """Move to the previous question."""
    global current_question
    if current_question > 0:
        current_question -= 1
        display_question(current_question)

def display_question(index):
    """Display the question and options for the current index."""
    for widget in question_frame.winfo_children():
        widget.destroy()  # Clear previous question

    # Display the question
    tk.Label(question_frame, text=questions[index], font=("Arial", 14, "bold"), anchor="w", bg="#f4f4f9").pack(fill="x", padx=20, pady=10)

    # Radio buttons for options
    var = question_vars[index]
    for option, value in options[index]:
        tk.Radiobutton(question_frame, text=option, variable=var, value=value, font=("Arial", 12), anchor="w", bg="#f4f4f9", activebackground="#e0e0e0").pack(anchor="w", padx=20, pady=5)

    # Show the navigation buttons
    if index > 0:
        prev_button.pack(side="left", padx=20, pady=10)
    if index < len(questions) - 1:
        next_button.pack(side="left", padx=20, pady=10)
    else:
        finish_button.pack(side="left", padx=20, pady=10)

# Main application
root = tk.Tk()
root.title("SIP Risk Analyzer")
root.state("zoomed")
root.configure(bg="#003366")

# Menubar
menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "SIP Risk Analyzer v1.0"))
menubar.add_cascade(label="Help", menu=help_menu)

# Add SIP Tracker project name in the menubar
menubar.add_command(label="SIP Tracker")

# Header
header = tk.Label(root, text="SIP Risk Analyzer", font=("Arial", 24, "bold"), fg="white", bg="#003366")
header.pack(fill="x", pady=20)

# Main content container
container = tk.Frame(root, bg="white", relief="solid", bd=2)
container.pack(fill="both", expand=True, padx=30, pady=10)

# Title within container
title_label = tk.Label(container, text="Risk Profile", font=("Arial", 18, "bold"))
title_label.pack(anchor="w", padx=20, pady=10)

# Question Frame (where questions will appear)
question_frame = tk.Frame(container, bg="#f4f4f9")
question_frame.pack(fill="both", expand=True, padx=20, pady=10)

# Footer
footer = tk.Label(root, text="Developed by [Your Name]", font=("Arial", 12), bg="#003366", fg="white")
footer.pack(fill="x", pady=10)

# Questions for risk assessment
questions = [
    "1. What is your primary investment goal?",
    "2. How do you react to market fluctuations?",
    "3. What is your investment time horizon?",
    "4. How much risk are you comfortable with in investments?",
    "5. How would you describe your knowledge of financial markets?"
]

# Options for each question and corresponding scores
options = [
    [("Preserve capital (1)", 1), ("Steady growth (2)", 2), ("High growth (3)", 3)],
    [("Very worried (1)", 1), ("Somewhat concerned (2)", 2), ("Not concerned (3)", 3)],
    [("Less than 3 years (1)", 1), ("3-5 years (2)", 2), ("More than 5 years (3)", 3)],
    [("Low (1)", 1), ("Moderate (2)", 2), ("High (3)", 3)],
    [("Beginner (1)", 1), ("Intermediate (2)", 2), ("Advanced (3)", 3)]
]

# Variable to store responses for each question
question_vars = [tk.IntVar(value=0) for _ in range(len(questions))]

# Initial question index
current_question = 0

# Navigation buttons with arrows
prev_button = tk.Button(container, text="← Previous", font=("Arial", 12), bg="#00b3b3", fg="white", command=previous_question, relief="raised", width=12)
next_button = tk.Button(container, text="Next →", font=("Arial", 12), bg="#00b3b3", fg="white", command=next_question, relief="raised", width=12)
finish_button = tk.Button(container, text="Finish & Calculate Risk", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", command=calculate_risk, relief="raised", width=18)

# Display the first question
display_question(current_question)

# Run the application
root.mainloop()
