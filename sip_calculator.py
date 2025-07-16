import tkinter as tk
from tkinter import messagebox, ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# --- Colors ---
HEADER_BG_COLOR = "navy"
LOGO_TEXT_COLOR = "white"
BTN_COLOR = "#4682B4"
BTN_TEXT_COLOR = "white"
CONTAINER_BG_COLOR = "#F0F8FF"
TEXT_COLOR = "navy"
ENTRY_BG_COLOR = "white"
LINE_COLOR = "#D3D3D3"  # Light Gray for the vertical line

# --- Functions ---
def go_back():
    root.destroy()
    import first_page  # Replace with actual navigation logic

def calculate_sip():
    try:
        years = int(years_entry.get())
        amount = int(amount_entry.get())
        rate = float(rate_combobox.get().strip('%')) / 100
        delay = int(delay_entry.get())
        
        # Future Value formula for SIP
        n = years * 12  # Number of months
        r = rate / 12   # Monthly rate of return
        future_value = amount * ((1 + r)**n - 1) * (1 + r) / r
        
        delayed_n = (years - delay) * 12
        delayed_future_value = amount * ((1 + r)**delayed_n - 1) * (1 + r) / r
        
        cost_of_delay = future_value - delayed_future_value

        # Display results
        result_label.config(text=f"₹ {future_value:,.2f}")
        delayed_result_label.config(text=f"₹ {delayed_future_value:,.2f}")
        cost_label.config(text=f"Cost of Delay: ₹ {cost_of_delay:,.2f}")

        # Display Invested and Estimated Amounts below the pie chart
        invested_label.config(text=f"Invested Amount: ₹ {amount:,.2f}")
        estimated_label.config(text=f"Estimated Amount: ₹ {future_value:,.2f}")

        # Update pie chart
        update_pie_chart(future_value, delayed_future_value)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for all fields.")

def update_pie_chart(total, delayed_total):
    labels = ['Original Investment', 'Delayed Investment']
    sizes = [total, delayed_total]
    colors = ['#4682B4', '#FF6347']
    explode = (0.1, 0)  # Explode the first slice

    ax.clear()
    ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    ax.set_title("Investment Comparison")

    canvas.draw()

# --- Initialize Main Window ---
root = tk.Tk()
root.title("SIP Investment Tracker - SIP Calculator")
root.state("zoomed")

# --- Menubar Setup ---
menubar = tk.Menu(root, bg=HEADER_BG_COLOR, fg="white", font=("Arial", 14))
menubar.add_command(label="Back", command=go_back)
# SIP Benefits Menu
menubar.add_command(label="SIP Benefits", command=lambda: show_message("SIP Benefits"))
menubar.add_command(label="🔍 FAQS", command=lambda: show_message("Search"))

# Plans Menu with Dropdown
plans_menu = tk.Menu(menubar, tearoff=0, bg=HEADER_BG_COLOR, fg="black", font=("Arial", 12))
plans_menu.add_command(label="SIP Calculator", command=lambda: show_message("SIP Calculator"))
plans_menu.add_command(label="Retirement Calculator", command=lambda: show_message("Retirement Calculator"))
plans_menu.add_command(label="Risk Analysis", command=lambda: show_message("Risk Analysis"))
plans_menu.add_separator()
plans_menu.add_command(label="Home", command=lambda: show_message("Home"))
plans_menu.add_command(label="Car", command=lambda: show_message("Car"))
plans_menu.add_command(label="Vacation", command=lambda: show_message("Vacation"))

# Add "Plans" to the menubar
menubar.add_cascade(label="Plans", menu=plans_menu)

root.config(menu=menubar)

# --- Header ---
def add_logo_title():
    logo_frame = tk.Frame(root, bg=HEADER_BG_COLOR, height=50)
    logo_frame.pack(fill="x")
    logo_label = tk.Label(logo_frame, text="SIP Tracker", font=("Arial", 16, "bold"), fg=LOGO_TEXT_COLOR, bg=HEADER_BG_COLOR)
    logo_label.pack(side="left", padx=20)

add_logo_title()

# --- Main Container ---
container = tk.Frame(root, bg=CONTAINER_BG_COLOR, pady=40, padx=40)
container.pack(expand=True, fill="both", pady=20, padx=20)

# --- SIP Calculator Heading ---
heading_label = tk.Label(container, text="SIP Calculator", font=("Arial", 24, "bold"), fg=TEXT_COLOR, bg=CONTAINER_BG_COLOR)
heading_label.pack(pady=20)

# --- Input Fields (Left) ---
input_frame = tk.Frame(container, bg=CONTAINER_BG_COLOR)
input_frame.pack(side="left", fill="y", padx=20)

def create_input_row(label_text, widget):
    row = tk.Frame(input_frame, bg=CONTAINER_BG_COLOR)
    row.pack(pady=15, fill="x")

    label = tk.Label(row, text=label_text, font=("Arial", 14), fg=TEXT_COLOR, bg=CONTAINER_BG_COLOR)
    label.pack(anchor="w")

    widget.pack(fill="x", pady=5, ipady=6)

# Entry fields and combobox
years_entry = tk.Entry(input_frame, font=("Arial", 12), bg=ENTRY_BG_COLOR)  # Reduced font size
amount_entry = tk.Entry(input_frame, font=("Arial", 12), bg=ENTRY_BG_COLOR)  # Reduced font size

rate_combobox = ttk.Combobox(input_frame, values=[f"{i}%" for i in range(5, 21)], font=("Arial", 12))  # Reduced font size
rate_combobox.set("10%")

delay_entry = tk.Entry(input_frame, font=("Arial", 12), bg=ENTRY_BG_COLOR)  # Reduced font size

create_input_row("Investment Duration (Years):", years_entry)
create_input_row("Investment Amount (₹):", amount_entry)
create_input_row("Expected Annual Rate of Return (%):", rate_combobox)
create_input_row("Delay in Investing (Years):", delay_entry)

# --- Calculate Button ---
calculate_btn = tk.Button(input_frame, text="Calculate SIP", font=("Arial", 14, "bold"), bg=BTN_COLOR, fg=BTN_TEXT_COLOR, command=calculate_sip)
calculate_btn.pack(pady=20)

# --- Pie Chart (Center) ---
chart_frame = tk.Frame(container, bg=CONTAINER_BG_COLOR)
chart_frame.pack(side="left", padx=50)

fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=chart_frame)
canvas.draw()
canvas.get_tk_widget().pack(pady=20)

# --- Vertical Line after Pie Chart ---
line_frame = tk.Frame(container, bg=LINE_COLOR, width=2, height=400)
line_frame.pack(side="left", padx=10, fill="y")

# --- Results and Cost of Delay (Right) ---
result_frame = tk.Frame(container, bg=CONTAINER_BG_COLOR)
result_frame.pack(side="left", fill="y", padx=20)

# --- Results and Cost of Delay (Right) ---
result_frame = tk.Frame(container, bg=CONTAINER_BG_COLOR)
result_frame.pack(side="left", fill="y", padx=20)

# Results Display
result_label = tk.Label(result_frame, text="Future Value: ₹ 0.00", font=("Arial", 16), fg=TEXT_COLOR, bg=CONTAINER_BG_COLOR)
result_label.pack(pady=10)

delayed_result_label = tk.Label(result_frame, text="Delayed Future Value: ₹ 0.00", font=("Arial", 16), fg=TEXT_COLOR, bg=CONTAINER_BG_COLOR)
delayed_result_label.pack(pady=10)

cost_label = tk.Label(result_frame, text="Cost of Delay: ₹ 0.00", font=("Arial", 16), fg="red", bg=CONTAINER_BG_COLOR)
cost_label.pack(pady=10)

# Invested and Estimated Amount Display
invested_label = tk.Label(result_frame, text="Invested Amount: ₹ 0.00", font=("Arial", 16), fg=TEXT_COLOR, bg=CONTAINER_BG_COLOR)
invested_label.pack(pady=10)

estimated_label = tk.Label(result_frame, text="Estimated Amount: ₹ 0.00", font=("Arial", 16), fg=TEXT_COLOR, bg=CONTAINER_BG_COLOR)
estimated_label.pack(pady=10)

# --- Footer ---
def add_footer():
    footer_label = tk.Label(root, text="© 2024 SIP Investment Tracker. All Rights Reserved.", font=("Arial", 12), bg=HEADER_BG_COLOR, fg=LOGO_TEXT_COLOR)
    footer_label.pack(side="bottom", fill="x")

add_footer()

# --- Main Application Loop ---
root.mainloop()
