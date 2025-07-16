import tkinter as tk
from tkinter import ttk, messagebox

# --- Colors ---
HEADER_BG_COLOR = "navy"
LOGO_TEXT_COLOR = "white"
BTN_COLOR = "#4682B4"
BTN_TEXT_COLOR = "white"
CONTAINER_BG_COLOR = "white"
TEXT_COLOR = "navy"
LINE_COLOR = "#4682B4"
ENTRY_BG_COLOR = "white"

# --- Functions ---
def remove_from_cart(item_label):
    """Remove an item from the cart"""
    item_label.destroy()
    messagebox.showinfo("Removed", "Fund removed from cart!")

def add_to_cart():
    """Add fund details to the cart"""
    fund_details = f"Amount: ₹{amount_entry.get()} | Frequency: {frequency_var.get()} | Duration: {duration_var.get()} Years"
    cart_item = tk.Label(cart_frame, text=fund_details, font=("Arial", 12), bg=CONTAINER_BG_COLOR, anchor="w")
    cart_item.pack(fill="x", pady=5)

    remove_button = tk.Button(cart_frame, text="Remove", command=lambda: remove_from_cart(cart_item), bg="#e74c3c", fg="white")
    remove_button.pack(side="right", padx=10, pady=5)

    # Reset the form after adding
    amount_entry.delete(0, tk.END)
    frequency_var.set('')
    duration_var.set('')

# --- Initialize Main Window ---
root = tk.Tk()
root.title("SIP Cart Page")
root.state("zoomed")

# --- Menubar Setup ---
menubar = tk.Menu(root, bg=HEADER_BG_COLOR, fg="white", font=("Arial", 14))
menubar.add_command(label="Back", command=root.quit)
menubar.add_command(label="SIP Benefits", command=lambda: messagebox.showinfo("SIP Benefits", "Learn about SIP."))
root.config(menu=menubar)

# --- Header with Logo ---
def add_logo_title():
    logo_frame = tk.Frame(root, bg=HEADER_BG_COLOR, height=50)
    logo_frame.pack(fill="x")
    logo_label = tk.Label(logo_frame, text="SIP Tracker - Cart", font=("Arial", 16, "bold"), fg=LOGO_TEXT_COLOR, bg=HEADER_BG_COLOR)
    logo_label.pack(side="left", padx=20)

add_logo_title()

# --- Main Title ---
def add_main_title():
    main_title = tk.Label(root, text="Your SIP Cart", font=("Arial", 24, "bold"), fg=TEXT_COLOR)
    main_title.pack(pady=(30, 20))

add_main_title()

# --- Cart Container ---
cart_frame = tk.Frame(root, bg=CONTAINER_BG_COLOR, pady=40, padx=40, relief="ridge", bd=2, height=400)
cart_frame.pack(fill="both", expand=True, padx=20)

# --- Fund Details Section ---
def add_fund_section():
    fund_frame = tk.Frame(root, bg=CONTAINER_BG_COLOR)
    fund_frame.pack(pady=(20, 50), padx=20)

    # Amount Entry
    amount_label = tk.Label(fund_frame, text="Amount (INR):", font=("Arial", 14), fg=TEXT_COLOR, bg=CONTAINER_BG_COLOR)
    amount_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    amount_entry = tk.Entry(fund_frame, font=("Arial", 14), bg=ENTRY_BG_COLOR, fg=TEXT_COLOR, width=30)
    amount_entry.grid(row=0, column=1, pady=10)

    # Frequency Dropdown
    frequency_label = tk.Label(fund_frame, text="Frequency:", font=("Arial", 14), fg=TEXT_COLOR, bg=CONTAINER_BG_COLOR)
    frequency_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    frequency_var = tk.StringVar()
    frequency_dropdown = ttk.Combobox(fund_frame, textvariable=frequency_var, values=["Monthly", "Quarterly", "Annually"], width=28)
    frequency_dropdown.grid(row=1, column=1, pady=10)

    # Duration Dropdown
    duration_label = tk.Label(fund_frame, text="Duration (Years):", font=("Arial", 14), fg=TEXT_COLOR, bg=CONTAINER_BG_COLOR)
    duration_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    duration_var = tk.StringVar()
    duration_dropdown = ttk.Combobox(fund_frame, textvariable=duration_var, values=["1", "2", "3", "5", "10"], width=28)
    duration_dropdown.grid(row=2, column=1, pady=10)

    # Add to Cart Button
    add_button = tk.Button(fund_frame, text="Add to Cart", command=lambda: add_to_cart(), bg=BTN_COLOR, fg=BTN_TEXT_COLOR)
    add_button.grid(row=3, column=0, columnspan=2, pady=20)

add_fund_section()

# --- Footer ---
def add_footer():
    footer_label = tk.Label(root, text="© 2024 SIP Tracker. All Rights Reserved.", font=("Arial", 12), bg=HEADER_BG_COLOR, fg=LOGO_TEXT_COLOR)
    footer_label.pack(side="bottom", fill="x")

add_footer()

# --- Main Application Loop ---
root.mainloop()
