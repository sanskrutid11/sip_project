import tkinter as tk
from tkinter import messagebox
import os

# --- Colors and Styles ---
HEADER_BG_COLOR = "navy blue"
HEADER_TEXT_COLOR = "white"
CONTAINER_BG_COLOR = "#F5FFFA"
FOOTER_BG_COLOR = "navy blue"
FOOTER_TEXT_COLOR = "white"
LABEL_TEXT_COLOR = "black"
FIELD_BG_COLOR = "#FAFAD2"
BTN_BG_COLOR = "#3CB371"
BTN_TEXT_COLOR = "white"
RESULT_BG_COLOR = "#228B22"
LINE_COLOR = "#A9A9A9"

# --- Functions ---
def go_back():
    messagebox.showinfo("Back", "Go back functionality is triggered.")

def calculate_investment():
    try:
        year = int(year_var.get())
        price = float(price_var.get())
        inflation = float(inflation_var.get())

        # Example calculation: Future Value with inflation
        future_price = price * ((1 + (inflation / 100)) ** (year - 2025))
        monthly_sip = future_price / ((year - 2025) * 12)

        result_label.config(text=f"Future Cost of Your Dream Home: ₹{future_price:,.2f}")
        investment_label.config(text=f"To afford your dream home of ₹{future_price:,.2f}:")
        sip_label.config(text=f"Monthly SIP Required: ₹{monthly_sip:,.2f}")

        result_section.pack(anchor="center", pady=20)  # Show result section dynamically

    except Exception as e:
        messagebox.showerror("Error", "Please enter valid inputs.")

def proceed_to_next_step():
    root.destroy()  # Close the current window
    os.system("python second_page.py")  # Open the second page

# --- Initialize Main Window ---
root = tk.Tk()
root.title("Home Planner")
root.state("zoomed")

# --- Menubar Setup ---
menubar = tk.Menu(root)
menubar.add_command(label="Back", command=go_back)
menubar.add_command(label="Home", command=lambda: messagebox.showinfo("Home", "Home menu clicked"))
menubar.add_command(label="About", command=lambda: messagebox.showinfo("About", "About menu clicked"))
menubar.add_command(label="FAQS", command=lambda: messagebox.showinfo("Contact Us menu clicked"))
root.config(menu=menubar)

# --- Header ---
header = tk.Frame(root, bg=HEADER_BG_COLOR, height=60)
header.pack(fill="x")
header_label = tk.Label(header, text="Dream Home Planner", font=("Arial", 24, "bold"), fg=HEADER_TEXT_COLOR, bg=HEADER_BG_COLOR)
header_label.pack(pady=10)

# --- Main Container ---
container = tk.Frame(root, bg=CONTAINER_BG_COLOR, padx=40, pady=20)
container.pack(expand=True, fill="both")

# Title in Container
container_title = tk.Label(
    container,
    text="Plan Your Dream Home Investment",
    font=("Arial", 24, "bold"),
    fg=LABEL_TEXT_COLOR,
    bg=CONTAINER_BG_COLOR
)
container_title.pack(anchor="center", pady=10)

line = tk.Frame(container, height=2, bg=LINE_COLOR)
line.pack(fill="x", pady=10)

# --- Input Section ---
input_frame = tk.Frame(container, bg=CONTAINER_BG_COLOR)
input_frame.pack(pady=20)

# Year
year_label = tk.Label(input_frame, text="I wish to buy my dream home in the year:", font=("Arial", 14), bg=CONTAINER_BG_COLOR, fg=LABEL_TEXT_COLOR)
year_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
year_var = tk.StringVar()
year_entry = tk.Entry(input_frame, textvariable=year_var, bg=FIELD_BG_COLOR, font=("Arial", 12))
year_entry.grid(row=0, column=1, padx=10, pady=10)

# Price
price_label = tk.Label(input_frame, text="Estimated price of the home (as per today):", font=("Arial", 14), bg=CONTAINER_BG_COLOR, fg=LABEL_TEXT_COLOR)
price_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
price_var = tk.StringVar()
price_entry = tk.Entry(input_frame, textvariable=price_var, bg=FIELD_BG_COLOR, font=("Arial", 12))
price_entry.grid(row=1, column=1, padx=10, pady=10)

# Inflation
inflation_label = tk.Label(input_frame, text="Expected rate of inflation (%):", font=("Arial", 14), bg=CONTAINER_BG_COLOR, fg=LABEL_TEXT_COLOR)
inflation_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
inflation_var = tk.StringVar()
inflation_entry = tk.Entry(input_frame, textvariable=inflation_var, bg=FIELD_BG_COLOR, font=("Arial", 12))
inflation_entry.grid(row=2, column=1, padx=10, pady=10)

# Calculate Button
calculate_btn = tk.Button(input_frame, text="Calculate", font=("Arial", 14, "bold"), bg=BTN_BG_COLOR, fg=BTN_TEXT_COLOR, command=calculate_investment)
calculate_btn.grid(row=3, column=0, columnspan=2, pady=20)

# --- Result Section (Initially Hidden) ---
result_section = tk.Frame(container, bg=CONTAINER_BG_COLOR)

# Result Box
result_frame = tk.Frame(result_section, bg=RESULT_BG_COLOR, bd=5, relief="ridge")
result_label = tk.Label(result_frame, text="", font=("Arial", 16), fg="white", bg=RESULT_BG_COLOR)
result_label.pack(pady=10)
result_frame.grid(row=0, column=0, columnspan=2, sticky="ew", padx=20, pady=10)

# Investment Label
investment_label = tk.Label(result_section, text="", font=("Arial", 14), bg=CONTAINER_BG_COLOR, fg=LABEL_TEXT_COLOR)
investment_label.grid(row=1, column=0, sticky="w", padx=20)

# SIP Label
sip_label = tk.Label(result_section, text="", font=("Arial", 14), bg=CONTAINER_BG_COLOR, fg=LABEL_TEXT_COLOR)
sip_label.grid(row=2, column=0, sticky="w", padx=20)

# Proceed Button
proceed_btn = tk.Button(result_section, text="Proceed", font=("Arial", 14, "bold"), bg=BTN_BG_COLOR, fg=BTN_TEXT_COLOR, command=proceed_to_next_step)
proceed_btn.grid(row=2, column=1, sticky="e", padx=20, pady=20)

# --- Footer ---
footer = tk.Frame(root, bg=FOOTER_BG_COLOR, height=30)
footer.pack(fill="x")
footer_label = tk.Label(footer, text="\u00A9 2025 Dream Home Planner. All Rights Reserved.", font=("Arial", 12), bg=FOOTER_BG_COLOR, fg=FOOTER_TEXT_COLOR)
footer_label.pack(pady=5)

# --- Main Loop ---
root.mainloop()
