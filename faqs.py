import tkinter as tk
from tkinter import messagebox

def request_callback():
    """Handle the Request Callback button click."""
    messagebox.showinfo("Callback Request", "We will contact you soon!")

# Main application
root = tk.Tk()
root.title("FAQs")
root.state("zoomed")  # Window size

# Menubar
menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "FAQ Section v1.0"))
menubar.add_cascade(label="Plans", menu=help_menu)

# Add SIP Tracker project name in the menubar
menubar.add_command(label="SIP Tracker")

# Header
header = tk.Label(root, text="Frequently Asked Questions", font=("Arial", 24, "bold"), fg="white", bg="#003366")
header.pack(fill="x", pady=20)

# Main content container
container = tk.Frame(root, bg="white", relief="solid", bd=2)
container.pack(fill="both", expand=True, padx=30, pady=10)

# FAQ Questions and Answers
faq_data = [
    ("What is SIP?", "SIP (Systematic Investment Plan) is a method of investing in mutual funds by contributing a fixed amount regularly."),
    ("How do I start an SIP?", "You can start an SIP by choosing a mutual fund and deciding the amount you want to invest monthly."),
    ("What is the minimum amount for SIP?", "The minimum SIP amount varies depending on the mutual fund, but typically starts at ₹500."),
    ("Can I stop my SIP anytime?", "Yes, you can cancel or modify your SIP at any time without any penalty."),
    ("What is the expected return from SIP?", "The return on an SIP depends on the performance of the mutual fund and the market conditions."),
]

# Create a list of answer widgets
answers = []

# Create the FAQ section with toggle functionality
for i, (question, answer_text) in enumerate(faq_data):
    # Question label
    question_frame = tk.Frame(container, bg="white")
    question_frame.pack(fill="x", padx=20, pady=5)
    
    question_label = tk.Label(question_frame, text=question, font=("Arial", 14), anchor="w", bg="white")
    question_label.pack(side="left", fill="x", padx=20, pady=5)

    # Answer label
    answer_label = tk.Label(container, text=answer_text, font=("Arial", 12), anchor="w", bg="white")
    answer_label.pack(fill="x", padx=20, pady=5)

# "Did not find what you were looking for?" Section
callback_section = tk.Frame(root, bg="#003366")
callback_section.pack(fill="x", padx=30, pady=20)

# Label and Request Callback button
callback_label = tk.Label(callback_section, text="Did not find what you were looking for?", font=("Arial", 14), fg="white", bg="#003366")
callback_label.pack(side="left", padx=10)

callback_button = tk.Button(callback_section, text="Request Callback", font=("Arial", 12, "bold"), bg="#00b3b3", fg="white", command=request_callback)
callback_button.pack(side="right", padx=10)

# Footer
footer = tk.Label(root, text="@2024 SIP Investment Tracker. All Rights Reserved.", font=("Arial", 12), bg="#003366", fg="white")
footer.pack(fill="x", pady=10)

# Run the application
root.mainloop()
