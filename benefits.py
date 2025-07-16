import tkinter as tk
from tkinter import messagebox
import subprocess


# --- Colors ---
HEADER_BG_COLOR = "white"
LOGO_TEXT_COLOR = "black"
CONTAINER_BG_COLOR = "white"
TEXT_COLOR = "navy"
BTN_COLOR = "#4682B4"
BTN_TEXT_COLOR = "white"
FOOTER_BG_COLOR = "#2F4F4F"
BLUE_GREEN = "#66CDAA"
BONE_COLOR = "#E3DAC9"

# --- Functions ---
def go_back():
    root.destroy()
    import add  # Replace with actual navigation logic

def open_second_page():
    root.destroy()
    import second_page  # Redirect to the second page script


def show_message(message):
    messagebox.showinfo("Menu", f"You clicked on {message}")

def open_funds_window():
    """Opens a new window to display the Funds section while keeping the main page content intact."""
    funds_window = tk.Toplevel(root)
    funds_window.title("Funds")
    funds_window.state("zoomed") 


# --- Initialize Main Window ---
root = tk.Tk()
root.title("SIP Benefits")
root.state("zoomed")

# --- Menubar Setup ---
menubar = tk.Menu(root, bg=HEADER_BG_COLOR, fg="white", font=("Arial", 14))
menubar.add_command(label="home", command=go_back)
menubar.add_command(label="SIP Benefits", command=lambda: show_message("SIP Benefits"))
menubar.add_command(label="🔍 FAQS", command=lambda: open_page("faqs"))

plans_menu = tk.Menu(menubar, tearoff=0, bg=HEADER_BG_COLOR, fg="black", font=("Arial", 12))
plans_menu.add_command(label="SIP Calculator", command=lambda: open_page("sip_calculator"))
plans_menu.add_command(label="Retirement Calculator", command=lambda: open_page("retirement"))
plans_menu.add_command(label="Risk Analysis", command=lambda: open_page("risk"))
plans_menu.add_separator()
plans_menu.add_command(label="Home", command=lambda: open_page("home"))
plans_menu.add_command(label="Car", command=lambda: open_page("car"))
plans_menu.add_command(label="Vacation", command=lambda: open_page("vacation"))
menubar.add_cascade(label="Plans", menu=plans_menu)
menubar.add_command(label="💼 Funds", command=open_funds_window)
menubar.add_command(label="📊 My Performance", command=lambda: open_page("investment_performance"))

root.config(menu=menubar)

# --- Header ---
def add_logo_title():
    logo_frame = tk.Frame(root, bg=HEADER_BG_COLOR, height=50)
    logo_frame.pack(fill="x")
    logo_label = tk.Label(logo_frame, text="SIP Tracker", font=("Arial", 16, "bold"), fg=LOGO_TEXT_COLOR, bg=HEADER_BG_COLOR)
    logo_label.pack(side="left", padx=20)
    journey_btn = tk.Button(logo_frame, text="Start Your Journey", font=("Arial", 12, "bold"), bg=BTN_COLOR, fg=BTN_TEXT_COLOR, command=open_second_page)
    journey_btn.pack(side="right", padx=20, pady=5)


add_logo_title()

# --- Main Container ---
container = tk.Frame(root, bg=CONTAINER_BG_COLOR, pady=40, padx=60)  # Added padding for left and right sides
container.pack(expand=True, fill="both", pady=20, padx=60)  # Ensure equal space on left and right

# --- SIP Benefits Title ---
def add_sip_benefits_title():
    title_label = tk.Label(container, text="Benefits of SIP", font=("Arial", 24, "bold"), fg=TEXT_COLOR, bg=CONTAINER_BG_COLOR)
    title_label.pack(pady=10)

    # Horizontal Line
    line = tk.Frame(container, height=2, bg=TEXT_COLOR)
    line.pack(fill="x", padx=20, pady=10)

add_sip_benefits_title()

# --- Investing via SIP Line ---
def add_investing_line():
    investing_label = tk.Label(container, text="Investing via an SIP in mutual funds offers the below benefits:", font=("Arial", 16), fg="black", bg=CONTAINER_BG_COLOR)
    investing_label.pack(pady=10)

add_investing_line()

# --- SIP Benefits Data ---
benefits = [
    {"title": "Disciplined Investing", "description": "Promotes a regular investment habit, and since the amount is auto-debited, it requires minimal monitoring.", "icon": "📈"},
    {"title": "Risk Mitigation", "description": "Averages out the impact of market volatility over time, allowing you to invest comfortably without worrying about timing the market.", "icon": "⚖️"},
    {"title": "Flexibility & Convenience", "description": "Allows both small and large investments. You can also pause, stop or top-up your SIP whenever you need to.", "icon": "🔄"},
    {"title": "Power of Compounding", "description": "If you opt for the growth option while investing, your profits get reinvested into the scheme. This way your wealth keeps growing.", "icon": "💰"}
]

# --- Display Benefits Horizontally with Icons and Design Enhancements ---
def display_benefits():
    for index, benefit in enumerate(benefits):
        # Alternate background colors for each card
        bg_color = BLUE_GREEN if index % 2 == 0 else BONE_COLOR

        card = tk.Frame(container, bg=bg_color, bd=2, relief="ridge", width=250, height=250)
        card.pack(side="left", padx=20, pady=20, ipadx=10, ipady=10)
        card.pack_propagate(False)  # Prevent shrinking to fit content

        # Icon in the Rectangle
        icon_label = tk.Label(card, text=benefit["icon"], font=("Arial", 30), bg=bg_color)
        icon_label.pack(pady=10)

        # Benefit Title
        title_label = tk.Label(card, text=benefit["title"], font=("Arial", 14, "bold"), fg=TEXT_COLOR, bg=bg_color)
        title_label.pack(pady=10)

        # Benefit Description
        desc_label = tk.Label(card, text=benefit["description"], font=("Arial", 12), wraplength=220, justify="center", fg="black", bg=bg_color)
        desc_label.pack(pady=10)

display_benefits()

def open_page(page_name):
    """Open a specific page based on the name."""
    try:
        subprocess.run(["python", f"{page_name}.py"])  # Open the corresponding page using subprocess
    except FileNotFoundError:
        messagebox.showerror("Error", f"{page_name}.py not found")


# --- Footer ---
def add_footer():
    footer_label = tk.Label(root, text="\u00A9 2024 SIP Investment Tracker. All Rights Reserved.", font=("Arial", 12), bg=FOOTER_BG_COLOR, fg=LOGO_TEXT_COLOR)
    footer_label.pack(side="bottom", fill="x")

add_footer()

# --- Main Application Loop ---
root.mainloop()
