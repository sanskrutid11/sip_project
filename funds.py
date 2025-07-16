import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random

# --- Colors ---
HEADER_BG_COLOR = "navy"
LOGO_TEXT_COLOR = "white"
BTN_COLOR = "#4682B4"
BTN_TEXT_COLOR = "white"
CONTAINER_BG_COLOR = "white"
TEXT_COLOR = "navy"
LINE_COLOR = "#4682B4"
CART_ICON_COLOR = "#FFA500"

# --- Initialize Main Window ---
root = tk.Tk()
root.title("SIP Investment Tracker")
root.state("zoomed")

# --- Global Cart ---
cart = []

# --- Mutual Fund Data ---
funds_data = [
    {"name": "UTI Aggressive Hybrid Fund", "category": "Hybrid", "nav": "₹433.5660", "risk": "Very High", "returns": "15.36%"},
    {"name": "UTI Arbitrage Fund", "category": "Hybrid", "nav": "₹35.8005", "risk": "Low", "returns": "7.14%"},
    {"name": "UTI Balanced Advantage Fund", "category": "Hybrid", "nav": "₹12.5011", "risk": "Moderately High", "returns": "18%"},
    {"name": "UTI Banking & Financial Services Fund", "category": "Equity", "nav": "₹202.3350", "risk": "Very High", "returns": "15.62%"},
    {"name": "UTI Banking & PSU Fund", "category": "Debt", "nav": "₹21.2561", "risk": "Moderate", "returns": "7.19%"},
    {"name": "UTI BSE Housing Index Fund", "category": "Index Fund", "nav": "₹15.7693", "risk": "Very High", "returns": "32.38%"},
]

# --- Functions ---
def go_back():
    show_main_page()

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def add_logo_title():
    logo_frame = tk.Frame(root, bg=HEADER_BG_COLOR, height=50)
    logo_frame.pack(fill="x")
    logo_label = tk.Label(logo_frame, text="SIP Tracker", font=("Arial", 16, "bold"), fg=LOGO_TEXT_COLOR, bg=HEADER_BG_COLOR)
    logo_label.pack(side="left", padx=20)
    
    cart_btn = tk.Button(logo_frame, text=f"Cart ({len(cart)})", font=("Arial", 14), bg=CART_ICON_COLOR, fg="white", command=view_cart)
    cart_btn.pack(side="right", padx=20)

def add_footer():
    footer_label = tk.Label(root, text="\u00a9 2024 SIP Investment Tracker. All Rights Reserved.", font=("Arial", 12), bg=HEADER_BG_COLOR, fg=LOGO_TEXT_COLOR)
    footer_label.pack(side="bottom", fill="x")

def add_main_title(title):
    main_title = tk.Label(root, text=title, font=("Arial", 24, "bold"), fg=TEXT_COLOR)
    main_title.pack(pady=(20, 10))

def add_to_cart(fund_name):
    cart.append(fund_name)
    messagebox.showinfo("Cart", f"{fund_name} has been added to your cart!")
    show_mutual_funds()  # Refresh the page to update cart count

def view_cart():
    clear_window()
    add_logo_title()
    add_main_title("Your Cart")
    
    if not cart:
        tk.Label(root, text="Your cart is empty.", font=("Arial", 16), fg=TEXT_COLOR).pack(pady=20)
    else:
        for item in cart:
            tk.Label(root, text=item, font=("Arial", 14), fg=TEXT_COLOR).pack(pady=5)
    
    tk.Button(root, text="Back", font=("Arial", 14, "bold"), bg=BTN_COLOR, fg=BTN_TEXT_COLOR, command=go_back).pack(pady=20)
    add_footer()

def show_mutual_funds():
    clear_window()
    add_logo_title()
    add_main_title("Mutual Funds")
    
    # Dropdown for Fund Type Selection
    fund_types = ["All", "Hybrid", "Equity", "Debt", "Index Fund"]
    selected_type = tk.StringVar(value="All")
    
    dropdown_frame = tk.Frame(root)
    dropdown_frame.pack(pady=10)
    tk.Label(dropdown_frame, text="Filter by Type:", font=("Arial", 14)).pack(side="left", padx=10)
    fund_dropdown = ttk.Combobox(dropdown_frame, values=fund_types, textvariable=selected_type, font=("Arial", 14))
    fund_dropdown.pack(side="left", padx=10)
    
    tk.Button(dropdown_frame, text="Filter", font=("Arial", 12), bg=BTN_COLOR, fg=BTN_TEXT_COLOR, command=lambda: display_funds(selected_type.get())).pack(side="left", padx=10)
    
    display_funds("All")

def display_funds(filter_type):
    # Clear existing funds display
    for widget in root.winfo_children():
        if isinstance(widget, tk.Frame) and widget != root.children['!frame']:
            widget.destroy()
    
    # Container for displaying funds
    container = tk.Frame(root, bg=CONTAINER_BG_COLOR)
    container.pack(pady=20, padx=20)
    
    filtered_funds = [fund for fund in funds_data if filter_type == "All" or fund["category"] == filter_type]
    
    for idx, fund in enumerate(filtered_funds):
        fund_frame = tk.Frame(container, bg="lightgrey", bd=2, relief="ridge", padx=20, pady=20)
        fund_frame.grid(row=idx // 2, column=idx % 2, padx=20, pady=20)
        
        # Fund Name
        tk.Label(fund_frame, text=fund["name"], font=("Arial", 16, "bold"), fg=TEXT_COLOR, wraplength=300, justify="center").pack(pady=10)
        
        # NAV and Risk
        tk.Label(fund_frame, text=f"NAV: {fund['nav']}", font=("Arial", 14)).pack(pady=5)
        tk.Label(fund_frame, text=f"Risk: {fund['risk']}", font=("Arial", 14)).pack(pady=5)
        
        # Returns
        tk.Label(fund_frame, text=f"Returns: {fund['returns']}", font=("Arial", 14)).pack(pady=5)
        
        # Add to Cart Button
        tk.Button(fund_frame, text="Add to Cart", font=("Arial", 12), bg=CART_ICON_COLOR, fg="white", command=lambda f=fund['name']: add_to_cart(f)).pack(pady=10)
    
    add_footer()

def show_main_page():
    clear_window()
    add_logo_title()
    add_main_title("Welcome to SIP Investment Tracker")
    
    tk.Button(root, text="View Mutual Funds", font=("Arial", 16, "bold"), bg=BTN_COLOR, fg=BTN_TEXT_COLOR, command=show_mutual_funds).pack(pady=50)
    
    add_footer()

# --- Run the Application ---
show_main_page()
root.mainloop()
