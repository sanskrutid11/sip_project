import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

# --- Colors ---
HEADER_BG_COLOR = "navy"
LOGO_TEXT_COLOR = "white"
BTN_COLOR = "#4682B4"
BTN_TEXT_COLOR = "white"
CONTAINER_BG_COLOR = "#F0F8FF"
TEXT_COLOR = "navy"
ENTRY_BG_COLOR = "white"
LINE_COLOR = "#4682B4"

# --- Initialize Main Window ---
root = tk.Tk()
root.title("SIP Investment Tracker")
root.state("zoomed")

# --- Global Cart List ---
cart = []

# --- Functions ---
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def add_logo_title():
    logo_frame = tk.Frame(root, bg=HEADER_BG_COLOR, height=50)
    logo_frame.pack(fill="x")
    logo_label = tk.Label(logo_frame, text="SIP Tracker", font=("Arial", 16, "bold"), fg=LOGO_TEXT_COLOR, bg=HEADER_BG_COLOR)
    logo_label.pack(side="left", padx=20)

def add_footer():
    footer_label = tk.Label(root, text="\u00a9 2024 SIP Investment Tracker. All Rights Reserved.", font=("Arial", 12), bg=HEADER_BG_COLOR, fg=LOGO_TEXT_COLOR)
    footer_label.pack(side="bottom", fill="x")

def add_main_title(title):
    main_title = tk.Label(root, text=title, font=("Arial", 24, "bold"), fg=TEXT_COLOR)
    main_title.pack(pady=(30, 20))

def validate_pan():
    messagebox.showinfo("Validate PAN", "PAN validated successfully!")
    show_goal_page()

def show_pan_page():
    clear_window()
    add_logo_title()
    add_main_title("Enter PAN and Start Your Journey")
    
    container = tk.Frame(root, bg=CONTAINER_BG_COLOR, pady=40, padx=40, relief="ridge", bd=2)
    container.pack(pady=(20, 50), padx=20)
    
    pan_frame = tk.Frame(container, bg=CONTAINER_BG_COLOR)
    pan_frame.pack(pady=(10, 20), fill="x")
    
    tk.Label(pan_frame, text="Enter PAN:", font=("Arial", 16, "bold"), fg=TEXT_COLOR, bg=CONTAINER_BG_COLOR).pack(side="left", padx=(0, 10))
    
    pan_entry = tk.Entry(pan_frame, font=("Arial", 14), bg=ENTRY_BG_COLOR, fg=TEXT_COLOR, relief="flat", justify="center", width=30)
    pan_entry.pack(side="left", fill="x", expand=True)
    
    tk.Frame(container, height=2, bg=LINE_COLOR).pack(fill="x", padx=10, pady=(0, 20))
    
    tk.Button(container, text="Validate", font=("Arial", 14, "bold"), bg=BTN_COLOR, fg=BTN_TEXT_COLOR, command=validate_pan, relief="flat", padx=20, pady=5).pack(pady=(10, 0))
    
    add_footer()

def show_goal_page():
    clear_window()
    add_logo_title()
    add_main_title("Select Your Goal and Risk Tolerance")
    
    container = tk.Frame(root, bg=CONTAINER_BG_COLOR, pady=40, padx=40)
    container.pack(pady=(20, 50), padx=20)
    
    goals = ["Short Term", "Moderate", "Long Term"]
    risk_levels = ["Low", "Medium", "High"]
    
    selected_goal = tk.StringVar()
    selected_risk = tk.StringVar()
    
    tk.Label(container, text="Select Goal:", font=("Arial", 16, "bold"), fg=TEXT_COLOR, bg=CONTAINER_BG_COLOR).pack(pady=10)
    goal_menu = ttk.Combobox(container, values=goals, textvariable=selected_goal, font=("Arial", 14))
    goal_menu.pack(pady=10)
    
    tk.Label(container, text="Select Risk Tolerance:", font=("Arial", 16, "bold"), fg=TEXT_COLOR, bg=CONTAINER_BG_COLOR).pack(pady=10)
    risk_menu = ttk.Combobox(container, values=risk_levels, textvariable=selected_risk, font=("Arial", 14))
    risk_menu.pack(pady=10)
    
    tk.Button(container, text="Show Mutual Funds", font=("Arial", 14, "bold"), bg=BTN_COLOR, fg=BTN_TEXT_COLOR, 
              command=lambda: show_mutual_funds(selected_goal.get(), selected_risk.get())).pack(pady=20)
    
    add_footer()

def add_to_cart(fund_name):
    cart.append(fund_name)
    messagebox.showinfo("Cart", f"{fund_name} added to cart!")

def show_mutual_funds(goal, risk):
    clear_window()
    add_logo_title()
    add_main_title(f"Mutual Funds for {goal} Goal and {risk} Risk")
    
    container = tk.Frame(root, bg=CONTAINER_BG_COLOR, pady=40, padx=40)
    container.pack(pady=(20, 50), padx=20)
    
    funds = {
        ("Short Term", "Low"): ["Fund A", "Fund B", "Fund C", "Fund D"],
        ("Moderate", "Medium"): ["Fund E", "Fund F", "Fund G", "Fund H"],
        ("Long Term", "High"): ["Fund I", "Fund J", "Fund K", "Fund L"]
    }
    
    fund_list = funds.get((goal, risk), ["No suitable funds found"])
    
    for i, fund in enumerate(fund_list):
        frame = tk.Frame(container, bg="white", relief="ridge", bd=2, padx=10, pady=10)
        frame.grid(row=i // 2, column=i % 2, padx=20, pady=20)
        
        icon = ImageTk.PhotoImage(Image.new("RGBA", (50, 50), "blue"))
        icon_label = tk.Label(frame, image=icon, bg="white")
        icon_label.image = icon  # Keep a reference
        icon_label.pack()
        
        tk.Label(frame, text=fund, font=("Arial", 16, "bold"), bg="white", fg=TEXT_COLOR).pack(pady=10)
        
        tk.Button(frame, text="Add to Cart", font=("Arial", 12), bg=BTN_COLOR, fg=BTN_TEXT_COLOR, 
                  command=lambda f=fund: add_to_cart(f)).pack(pady=10)
    
    add_footer()

# --- Run the Application ---
show_pan_page()
root.mainloop()