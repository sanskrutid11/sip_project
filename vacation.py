import tkinter as tk
from tkinter import messagebox

# --- Colors ---
HEADER_BG_COLOR = "navy"
LOGO_TEXT_COLOR = "white"
CONTAINER_BG_COLOR = "white"
BTN_COLOR = "#4682B4"
BTN_TEXT_COLOR = "white"
FOOTER_BG_COLOR = "#2F4F4F"
LABEL_TEXT_COLOR = "black"
FIELD_BG_COLOR = "#F0F8FF"
RESULT_BG_COLOR = "#1E3A8A"  # Navy blue for the result rectangle
LINE_COLOR = "#A9A9A9"  # Light gray for the line

# --- Functions ---
def go_back():
    root.destroy()
    import first_page  # Replace with actual navigation logic

def show_message(message):
    messagebox.showinfo("Menu", f"You clicked on {message}")

def calculate_vacation_cost():
    try:
        month = int(month_var.get())
        year = int(year_var.get())
        cost = float(cost_var.get())
        rate = float(rate_var.get())
        risk = risk_var.get()

        # Example calculation: Future Value
        total = cost * ((1 + (rate / 100)) ** (year - 2025))

        # Calculate the monthly SIP needed
        months = (year - 2025) * 12
        sip_required = total / months

        result_label.config(text=f"Total Amount for Dream Vacation: ₹{total:,.2f}")
        investment_label.config(text=f"To achieve your goal of ₹{total:,.2f} in {year - 2025} years, you may need to invest:")
        sip_label.config(text=f"Monthly SIP required: ₹{sip_required:,.2f}")
        
        result_section.pack(pady=20)
        proceed_btn.pack(pady=10)

    except Exception as e:
        messagebox.showerror("Error", "Please enter valid inputs.")

def proceed_to_second_page():
    root.destroy()  # Close the current window
    import second_page  # Implement navigation logic

# --- Initialize Main Window ---
root = tk.Tk()
root.title("Dream Vacation Planner")
root.state("zoomed")

# --- Menubar Setup ---
menubar = tk.Menu(root, bg=HEADER_BG_COLOR, fg="white", font=("Arial", 14))
menubar.add_command(label="Back", command=go_back)
menubar.add_command(label="Home", command=lambda: show_message("Home"))
menubar.add_command(label="About", command=lambda: show_message("About"))
menubar.add_command(label="FAQS", command=lambda: show_message("Contact Us"))
root.config(menu=menubar)

# --- Header ---
def add_logo_title():
    logo_frame = tk.Frame(root, bg=HEADER_BG_COLOR, height=50)
    logo_frame.pack(fill="x")
    logo_label = tk.Label(logo_frame, text="Dream Vacation Planner", font=("Arial", 18, "bold"), fg=LOGO_TEXT_COLOR, bg=HEADER_BG_COLOR)
    logo_label.pack(side="left", padx=20)

add_logo_title()

# --- Main Container ---
container = tk.Frame(root, bg=CONTAINER_BG_COLOR, pady=20, padx=40)
container.pack(expand=True, fill="both", pady=20)

# --- Title ---
title_label = tk.Label(container, text="Plan Your Dream Vacation", font=("Arial", 24, "bold"), fg=LABEL_TEXT_COLOR, bg=CONTAINER_BG_COLOR)
title_label.pack(pady=10)

# --- Horizontal Line Below Title ---
line = tk.Frame(container, height=2, bg=LINE_COLOR)
line.pack(fill="x", padx=40, pady=10)

# --- Input Fields ---
input_frame = tk.Frame(container, bg=CONTAINER_BG_COLOR)
input_frame.pack(pady=10)

# Month
month_label = tk.Label(input_frame, text="Month (1-12):", font=("Arial", 14), fg=LABEL_TEXT_COLOR, bg=CONTAINER_BG_COLOR)
month_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
month_var = tk.StringVar()
month_entry = tk.Entry(input_frame, textvariable=month_var, bg=FIELD_BG_COLOR, font=("Arial", 12))
month_entry.grid(row=0, column=1, padx=10, pady=10)

# Year
year_label = tk.Label(input_frame, text="Year:", font=("Arial", 14), fg=LABEL_TEXT_COLOR, bg=CONTAINER_BG_COLOR)
year_label.grid(row=0, column=2, padx=10, pady=10, sticky="w")
year_var = tk.StringVar()
year_entry = tk.Entry(input_frame, textvariable=year_var, bg=FIELD_BG_COLOR, font=("Arial", 12))
year_entry.grid(row=0, column=3, padx=10, pady=10)

# Vacation Cost
cost_label = tk.Label(input_frame, text="Dream Vacation Cost (₹):", font=("Arial", 14), fg=LABEL_TEXT_COLOR, bg=CONTAINER_BG_COLOR)
cost_label.grid(row=0, column=4, padx=10, pady=10, sticky="w")
cost_var = tk.StringVar()
cost_entry = tk.Entry(input_frame, textvariable=cost_var, bg=FIELD_BG_COLOR, font=("Arial", 12))
cost_entry.grid(row=0, column=5, padx=10, pady=10)

# Expected Rate of Return
rate_label = tk.Label(input_frame, text="Expected Rate of Return (%):", font=("Arial", 14), fg=LABEL_TEXT_COLOR, bg=CONTAINER_BG_COLOR)
rate_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
rate_var = tk.StringVar()
rate_entry = tk.Entry(input_frame, textvariable=rate_var, bg=FIELD_BG_COLOR, font=("Arial", 12))
rate_entry.grid(row=1, column=1, padx=10, pady=10)

# Risk Profile
risk_label = tk.Label(input_frame, text="My Risk Profile Is:", font=("Arial", 14), fg=LABEL_TEXT_COLOR, bg=CONTAINER_BG_COLOR)
risk_label.grid(row=1, column=2, padx=10, pady=10, sticky="w")
risk_var = tk.StringVar()
risk_dropdown = tk.OptionMenu(input_frame, risk_var, "Low", "Medium", "High")
risk_dropdown.config(bg=FIELD_BG_COLOR, font=("Arial", 12))
risk_var.set("Medium")
risk_dropdown.grid(row=1, column=3, padx=10, pady=10)

# Calculate Button
calculate_btn = tk.Button(input_frame, text="Calculate", font=("Arial", 14, "bold"), bg=BTN_COLOR, fg=BTN_TEXT_COLOR, command=calculate_vacation_cost)
calculate_btn.grid(row=1, column=4, padx=10, pady=10)

# --- Result Section ---
result_section = tk.Frame(container, bg=CONTAINER_BG_COLOR)
result_heading = tk.Label(result_section, text="Dream Vacation Plan Results", font=("Arial", 20, "bold"), fg=LABEL_TEXT_COLOR, bg=CONTAINER_BG_COLOR)
result_heading.pack()

result_frame = tk.Frame(result_section, bg=RESULT_BG_COLOR, bd=5, relief="ridge")
result_label = tk.Label(result_frame, text="", font=("Arial", 16), fg="white", bg=RESULT_BG_COLOR)
result_label.pack(pady=10)
result_frame.pack(pady=10, fill="x", padx=40)

investment_label = tk.Label(result_section, text="", font=("Arial", 14), fg=LABEL_TEXT_COLOR, bg=CONTAINER_BG_COLOR)
investment_label.pack(pady=5)

sip_label = tk.Label(result_section, text="", font=("Arial", 14), fg=LABEL_TEXT_COLOR, bg=CONTAINER_BG_COLOR)
sip_label.pack(pady=5)

# Proceed Button
proceed_btn = tk.Button(container, text="Proceed", font=("Arial", 14, "bold"), bg=BTN_COLOR, fg=BTN_TEXT_COLOR, command=proceed_to_second_page)

# --- Footer ---
def add_footer():
    footer_label = tk.Label(root, text="© 2024 SIP Investment Tracker. All Rights Reserved.", font=("Arial", 12), bg=FOOTER_BG_COLOR, fg=LOGO_TEXT_COLOR)
    footer_label.pack(side="bottom", fill="x")

add_footer()

# --- Main Application Loop ---
root.mainloop()
