import tkinter as tk
from tkinter import messagebox
import subprocess
from tkinter import PhotoImage
from PIL import Image, ImageTk

# --- Colors ---
HEADER_BG_COLOR = "white"
LOGO_TEXT_COLOR = "black"
BTN_COLOR = "navy blue"
BTN_TEXT_COLOR = "white"
CONTAINER_BG_COLOR = "#F5DEB3"  # Light brown color
TITLE_COLOR = "navy blue"
NAVY_BLUE = "#000080"  # Navy blue for specific text
TEXT_COLOR = "black"

# --- Functions ---
def open_second_page():
    root.destroy()
    import second_page  # Redirect to the second page script

def show_message(option):
    messagebox.showinfo(option, f"Selected: {option}")

def open_funds_window():
    """Opens a new window to display the Funds section while keeping the main page content intact."""
    funds_window = tk.Toplevel(root)
    funds_window.title("Funds")
    funds_window.state("zoomed") 

    # --- Menubar Setup for Funds Window ---
    menubar = tk.Menu(funds_window, bg=HEADER_BG_COLOR, fg="black", font=("Arial", 14))
    
    menubar.add_command(label="Admin", command=lambda: open_page("admin"))
    menubar.add_command(label="SIP Benefits", command=lambda: open_page("benefits"))
    menubar.add_command(label="🔍 FAQS", command=lambda: open_page("faqs"))

     # Plans Menu with Dropdown
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

    funds_window.config(menu=menubar)

    # --- Header with Logo ---
    logo_frame = tk.Frame(funds_window, bg=HEADER_BG_COLOR, height=50)
    logo_frame.pack(fill="x")
    logo_label = tk.Label(logo_frame, text="SIP Tracker", font=("Arial", 16, "bold"), fg=LOGO_TEXT_COLOR, bg=HEADER_BG_COLOR)
    logo_label.pack(side="left", padx=20)
    journey_btn = tk.Button(logo_frame, text="Start Your Journey", font=("Arial", 12, "bold"), bg=BTN_COLOR, fg=BTN_TEXT_COLOR, command=open_second_page)
    journey_btn.pack(side="right", padx=20, pady=5)

    # --- Main Content for Funds Window ---
    container = tk.Frame(funds_window, bg=CONTAINER_BG_COLOR, pady=20, padx=20)
    container.pack(fill="both", expand=True, pady=20, padx=20)

    tk.Label(container, text="Select a Mutual Fund Type", font=("Arial", 18, "bold"), bg=CONTAINER_BG_COLOR).pack(pady=10)

    # Types of Funds in Horizontal Layout
    types_of_funds = ["Equity Funds", "Debt Funds", "Hybrid Funds", "Index Funds", "ELSS Funds", "Liquid Funds"]

    header_frame = tk.Frame(container, bg=CONTAINER_BG_COLOR)
    header_frame.pack(pady=10)

    # Frame to display fund details in horizontal direction
    funds_frame = tk.Frame(container, bg=CONTAINER_BG_COLOR)
    funds_frame.pack(fill="both", expand=True)

    # Sample data for each fund type
    fund_data = {
        "Equity Funds": [
            {"name": "Equity Growth Fund", "desc": "High growth potential with higher risk.", "price": "₹5000", "risk": "High", "return": "15%"},
            {"name": "Bluechip Equity Fund", "desc": "Invests in top-performing companies.", "price": "₹3000", "risk": "Moderate", "return": "12%"},
            {"name": "Midcap Equity Fund", "desc": "Focuses on mid-sized companies.", "price": "₹2000", "risk": "Moderate", "return": "13%"},
        ],
        "Debt Funds": [
            {"name": "Short-Term Debt Fund", "desc": "For short-term investments with low risk.", "price": "₹400", "risk": "Low", "return": "7%"},
            {"name": "Corporate Bond Fund", "desc": "Invests in corporate bonds.", "price": "₹250", "risk": "Low", "return": "8%"},
            {"name": "Government Securities Fund", "desc": "Invests in government bonds.", "price": "₹500", "risk": "Low", "return": "6%"},
        ],
        "Hybrid Funds": [
            {"name": "Aggressive Hybrid Fund", "desc": "Mix of equity and debt for high returns.", "price": "₹9000", "risk": "High", "return": "14%"},
            {"name": "Balanced Advantage Fund", "desc": "Balances risk and reward.", "price": "₹8000", "risk": "Moderate", "return": "10%"},
            {"name": "Conservative Hybrid Fund", "desc": "Lower risk with debt dominance.", "price": "₹7000", "risk": "Low", "return": "8%"},
        ],
        "Index Funds": [
            {"name": "NIFTY 50 Index Fund", "desc": "Tracks NIFTY 50 index.", "price": "₹6000", "risk": "Moderate", "return": "10%"},
            {"name": "SENSEX Index Fund", "desc": "Tracks SENSEX index.", "price": "₹6500", "risk": "Moderate", "return": "9%"},
            {"name": "Midcap Index Fund", "desc": "Invests in midcap index companies.", "price": "₹7500", "risk": "High", "return": "12%"},
        ],
        "ELSS Funds": [
            {"name": "Tax Saver ELSS Fund", "desc": "Equity-linked saving scheme for tax benefits.", "price": "₹5000", "risk": "High", "return": "15%"},
            {"name": "Growth ELSS Fund", "desc": "High growth with tax savings.", "price": "₹1000", "risk": "Moderate", "return": "13%"},
            {"name": "Balanced ELSS Fund", "desc": "Mix of equity and debt with tax benefits.", "price": "₹1500", "risk": "Moderate", "return": "10%"},
        ],
        "Liquid Funds": [
            {"name": "Overnight Fund", "desc": "Invests in overnight securities.", "price": "₹300", "risk": "Low", "return": "6%"},
            {"name": "Liquid Growth Fund", "desc": "Growth-oriented liquid investments.", "price": "₹500", "risk": "Low", "return": "7%"},
            {"name": "Treasury Liquid Fund", "desc": "Invests in treasury bills.", "price": "₹400", "risk": "Low", "return": "5%"},
        ]
    }

    def display_funds(fund_type):
        """Display fund details for the selected type in horizontal layout."""
        # Clear previous content
        for widget in funds_frame.winfo_children():
            widget.destroy()

        tk.Label(funds_frame, text=f"{fund_type}", font=("Arial", 18, "bold"), bg=CONTAINER_BG_COLOR).pack(pady=10)

        # Horizontal line after fund type
        line_frame = tk.Frame(funds_frame, bg="black", height=2)
        line_frame.pack(fill="x", pady=10)

        # Retrieve relevant funds
        funds = fund_data.get(fund_type, [])

        # Create a canvas and a horizontal scrollbar
        canvas = tk.Canvas(funds_frame, bg=CONTAINER_BG_COLOR)
        scrollbar = tk.Scrollbar(funds_frame, orient="horizontal", command=canvas.xview)
        canvas.configure(xscrollcommand=scrollbar.set)

        # Create a frame within the canvas to hold the funds
        scrollable_frame = tk.Frame(canvas, bg=CONTAINER_BG_COLOR)

        # Add funds to the scrollable frame in horizontal direction
        for index, fund in enumerate(funds):
            frame = tk.Frame(scrollable_frame, bg="white", relief="solid", bd=2, padx=20, pady=20)
            frame.grid(row=0, column=index, padx=15, pady=15, sticky="nsew", ipadx=10, ipady=10)

            # --- Upper Part: Fund Name, Cart Icon, and Arrow Icon ---
            upper_frame = tk.Frame(frame, bg="white")
            upper_frame.pack(fill="x", pady=(0, 10))

            tk.Label(upper_frame, text=fund["name"], font=("Arial", 14, "bold"), bg="white").pack(side="left", padx=(0, 5))
            arrow_btn = tk.Button(upper_frame, text="➡️", font=("Arial", 12), bg=BTN_COLOR, fg=BTN_TEXT_COLOR, command=lambda f=fund: open_detailed_page(f))
            arrow_btn.pack(side="right")

            # --- Middle Part: Price, Risk, and Horizontal Line ---
            middle_frame = tk.Frame(frame, bg="white")
            middle_frame.pack(fill="x", pady=(0, 10))

            tk.Label(middle_frame, text=f"Price: {fund['price']}", font=("Arial", 12), bg="white").pack(anchor="w")
            tk.Label(middle_frame, text=f"Risk: {fund['risk']}", font=("Arial", 12), bg="white").pack(anchor="w")

            # Horizontal line
            tk.Frame(middle_frame, bg="black", height=1).pack(fill="x", pady=5)

            # --- Lower Part: Returns and 'Start SIP' Button ---
            lower_frame = tk.Frame(frame, bg="white")
            lower_frame.pack(fill="x")

            tk.Label(lower_frame, text=f"Return: {fund['return']}", font=("Arial", 12), bg="white").pack(pady=(0, 10))
            start_sip_btn = tk.Button(lower_frame, text="Start SIP", font=("Arial", 12, "bold"), bg=BTN_COLOR, fg=BTN_TEXT_COLOR, command=lambda: show_message("Start SIP"))
            start_sip_btn.pack()

        # Update canvas window
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        # Configure the scrollbar
        scrollable_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        canvas.pack(fill="both", expand=True)
        scrollbar.pack(fill="x")

    # Create buttons for each type of fund
    for fund_type in types_of_funds:
        btn = tk.Button(header_frame, text=fund_type, font=("Arial", 12, "bold"), bg=BTN_COLOR, fg=BTN_TEXT_COLOR,
                        command=lambda f=fund_type: display_funds(f))
        btn.pack(side="left", padx=10)

    # Display default fund type on window open
    display_funds("Equity Funds")

    # --- Footer for Funds Window ---
    footer_label = tk.Label(funds_window, text="© 2024 SIP Investment Tracker. All Rights Reserved.",
                            font=("Arial", 12), bg=HEADER_BG_COLOR, fg="black")
    footer_label.pack(side="bottom", fill="x")

def open_page(page_name):
    """Open a specific page based on the name."""
    try:
        subprocess.run(["python", f"{page_name}.py"])  # Open the corresponding page using subprocess
    except FileNotFoundError:
        messagebox.showerror("Error", f"{page_name}.py not found")

def open_detailed_page(fund):
    """Opens the detailed description page for the selected fund."""
    import detailed_page
    detailed_page.open_detailed_page(fund)

# --- Initialize Main Window ---
root = tk.Tk()
root.title("SIP Investment Tracker")
root.state("zoomed")

# --- Menubar Setup ---
menubar = tk.Menu(root, bg=HEADER_BG_COLOR, fg="black", font=("Arial", 14))

menubar.add_command(label="Admin", command=lambda: open_page("admin"))
menubar.add_command(label="SIP Benefits", command=lambda: open_page("benefits"))
menubar.add_command(label="🔍 FAQS", command=lambda: open_page("faqs"))

# Plans Menu with Dropdown
plans_menu = tk.Menu(menubar, tearoff=0, bg=HEADER_BG_COLOR, fg="black", font=("Arial", 12))
plans_menu.add_command(label="SIP Calculator", command=lambda: open_page("sip_calculator"))
plans_menu.add_command(label="Retirement Calculator", command=lambda: open_page("retirement"))
plans_menu.add_command(label="Risk Analysis", command=lambda: open_page("risk"))
plans_menu.add_separator()
plans_menu.add_command(label="Home",  command=lambda: open_page("home"))
plans_menu.add_command(label="Car", command=lambda: open_page("car"))
plans_menu.add_command(label="Vacation",command=lambda: open_page("vacation"))

menubar.add_cascade(label="Plans", menu=plans_menu)
menubar.add_command(label="💼 Funds", command=open_funds_window)
menubar.add_command(label="📊 My Performance", command=lambda: open_page("investment_performance"))

root.config(menu=menubar)
# --- Header with Logo ---
def add_logo_title():
    logo_frame = tk.Frame(root, bg=HEADER_BG_COLOR, height=50)
    logo_frame.pack(fill="x")
    logo_label = tk.Label(logo_frame, text="SIP Tracker", font=("Arial", 16, "bold"), fg=LOGO_TEXT_COLOR, bg=HEADER_BG_COLOR)
    logo_label.pack(side="left", padx=20)
    journey_btn = tk.Button(logo_frame, text="Start Your Journey", font=("Arial", 12, "bold"), bg=BTN_COLOR, fg=BTN_TEXT_COLOR, command=open_second_page)
    journey_btn.pack(side="right", padx=20, pady=5)

add_logo_title()

def add_sip_section():
    # Create the main container with a border for a polished look
    container = tk.Frame(root, bg=CONTAINER_BG_COLOR, pady=20, padx=20, relief="solid", bd=2)
    container.pack(fill="both", expand=True, pady=20, padx=20)

    # Text Frame (Left Side)
    text_frame = tk.Frame(container, bg=CONTAINER_BG_COLOR, padx=20, pady=10)
    text_frame.pack(side="left", fill="both", expand=True, padx=(0, 10), pady=10)

    sip_label = tk.Label(
        text_frame,
        text="WHAT IS A SYSTEMATIC INVESTMENT PLAN (SIP) IN MUTUAL FUNDS?",
        font=("Arial", 20, "bold"),
        fg=TITLE_COLOR,
        bg=CONTAINER_BG_COLOR,
        wraplength=600,
        justify="left"
    )
    sip_label.pack(anchor="nw", pady=(10, 20))

    description = (
        "You may have heard or seen SIP in a lot of advertisements online as well as offline and wondered "
        "“What is an SIP?” To explain in simple terms, a Systematic Investment Plan (SIP) allows you to invest "
        "through instalments in mutual funds. If you wish to invest in a staggered manner regularly, then SIP is "
        "the way to go. It allows you to invest small, periodic amounts, making wealth creation more accessible "
        "and disciplined.\n\n"
        "Mutual fund SIPs offer financial stability through consistent investments over time. You can start with "
        "a small amount such as ₹500*, or even higher as per your budget and financial goal. Over time, you can "
        "top up your existing SIP or start a new SIP in another mutual fund as and when needed. SIPs also allow "
        "you to pause your instalments in case you need to. You can restart your SIP once you are ready to invest again."
    )

    description_label = tk.Label(
        text_frame,
        text=description,
        font=("Arial", 16),
        fg=TEXT_COLOR,
        bg=CONTAINER_BG_COLOR,
        wraplength=600,
        justify="left"
    )
    description_label.pack(anchor="nw", pady=(0, 10))

    # Image Frame (Right Side)
    image_frame = tk.Frame(container, bg=CONTAINER_BG_COLOR, padx=20, pady=10)
    image_frame.pack(side="left", fill="both", expand=True)

    # Load and Resize Image
    image_path = "sip.png"  # Adjust path as necessary
    try:
        original_image = Image.open(image_path)

        # Resize image dynamically to fit
        resized_image = original_image.resize((500, 500), Image.Resampling.LANCZOS)
        sip = ImageTk.PhotoImage(resized_image)

        # Display the image
        image_label = tk.Label(image_frame, image=sip, bg=CONTAINER_BG_COLOR)
        image_label.image = sip  # Keep a reference
        image_label.pack(anchor="center", pady=(10, 20))
    except Exception as e:
        print(f"Error loading image: {e}")
        error_label = tk.Label(
            image_frame,
            text="Image not found",
            font=("Arial", 14, "italic"),
            fg="red",
            bg=CONTAINER_BG_COLOR
        )
        error_label.pack(anchor="center", pady=(10, 20))

    # Bottom Button Frame
    button_frame = tk.Frame(container, bg=CONTAINER_BG_COLOR)
    button_frame.pack(fill="x", pady=(10, 20))

    # Add Start SIP Button (Centered)
    start_sip_button = tk.Button(
        container,
        text="Start SIP",
        font=("Arial", 14, "bold"),
        bg="navy blue",
        fg="white",
        command=lambda: open_page("second_page")  # Replace with navigation logic
    )
    start_sip_button.place(relx=0.5, rely=0.95, anchor="center")

add_sip_section()

# --- Footer ---
def add_footer():
    footer_label = tk.Label(
        root,
        text="© 2024 SIP Investment Tracker. All Rights Reserved.",
        font=("Arial", 12),
        bg=HEADER_BG_COLOR,
        fg="black"
    )
    footer_label.pack(side="bottom", fill="x")

add_footer()


root.mainloop()
